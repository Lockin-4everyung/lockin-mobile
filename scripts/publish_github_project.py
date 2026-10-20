"""Publish reviewed milestones/issues/views for LockIn Project #1, preserving assignees."""
import csv
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "planning/github"
STATE_FILE = PACKAGE / "published-state.json"
PLAN = json.loads((PACKAGE / "publication-plan.json").read_text(encoding="utf-8"))
ORG, REPO = PLAN["organization"], PLAN["repository"]
TARGET = f"{ORG}/{REPO}"
PROJECT_PATH = f"orgs/{ORG}/projectsV2/{PLAN['project_number']}"
HEADER = ["-H", "X-GitHub-Api-Version: 2026-03-10"]


def api(endpoint, method="GET", payload=None):
    args = ["gh", "api", endpoint, "--method", method, *HEADER]
    if payload is not None:
        args += ["--input", "-"]
    result = subprocess.run(
        args, input=json.dumps(payload, ensure_ascii=False) if payload is not None else None,
        capture_output=True, text=True, encoding="utf-8", cwd=ROOT
    )
    if result.returncode:
        raise RuntimeError(f"{method} {endpoint}: {result.stderr.strip()}")
    return json.loads(result.stdout) if result.stdout.strip() else None


def gql(query, **variables):
    response = api("graphql", "POST", {"query": query, "variables": variables})
    if response.get("errors"):
        raise RuntimeError(json.dumps(response["errors"], ensure_ascii=False))
    return response["data"]


def save(state):
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


QUERY = """
query($org:String!, $repo:String!, $number:Int!){
 viewer{login}
 repository(owner:$org,name:$repo){id viewerPermission}
 organization(login:$org){projectV2(number:$number){
  id title url public viewerCanUpdate
  views(first:50){nodes{id number name layout}}
  fields(first:50){nodes{
   ... on ProjectV2Field{id name}
   ... on ProjectV2SingleSelectField{id name options{id name}}
  }}
  items(first:100){nodes{id content{... on Issue{id number title}}}}
 }}
}
"""


def main():
    data = gql(QUERY, org=ORG, repo=REPO, number=PLAN["project_number"])
    project = data["organization"]["projectV2"]
    permission = data["repository"]["viewerPermission"]
    if permission not in ("WRITE", "MAINTAIN", "ADMIN") or not project["viewerCanUpdate"]:
        raise RuntimeError("Need repository write and Project write before publishing.")
    print("Authenticated:", data["viewer"]["login"], "| repo:", permission, flush=True)
    state = {"project_url": project["url"], "project_id": project["id"],
             "status": "in_progress", "assignees": "See planning/team.json; preserve existing assignments",
             "milestones": {}, "issues": {}, "views": project["views"]["nodes"]}
    save(state)
    milestones = api(f"repos/{TARGET}/milestones?state=all&per_page=100")
    for milestone in PLAN["milestones"]:
        found = next((m for m in milestones if m["title"] == milestone["title"]), None)
        if found is None:
            found = api(f"repos/{TARGET}/milestones", "POST",
                        {"title": milestone["title"], "description": milestone["description"]})
            milestones.append(found)
        state["milestones"][milestone["key"]] = {
            "number": found["number"], "title": found["title"], "url": found["html_url"]}
        save(state)
        print("Milestone:", found["title"], flush=True)
    issues = api(f"repos/{TARGET}/issues?state=all&per_page=100")
    items = {node["content"]["id"]: node["id"] for node in project["items"]["nodes"]
             if node.get("content") and node["content"].get("id")}
    status_field = next(f for f in project["fields"]["nodes"] if f["name"] == "Status")
    options = {o["name"]: o["id"] for o in status_field["options"]}
    for task in PLAN["issues"]:
        task_id = task["task_id"]
        matches = [i for i in issues if i["title"].startswith(f"[{task_id}]") and "pull_request" not in i]
        if len(matches) > 1:
            raise RuntimeError(f"Multiple issues match {task_id}; refusing to guess.")
        issue = matches[0] if matches else api(
            f"repos/{TARGET}/issues", "POST",
            {"title": task["title"],
             "body": (PACKAGE / task["body_file"]).read_text(encoding="utf-8"),
             "milestone": state["milestones"][task["milestone_key"]]["number"],
             "assignees": task.get("assignees", [])}
        )
        if not matches:
            issues.append(issue)
        item_id = items.get(issue["node_id"])
        if not item_id:
            result = gql("""
mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p,contentId:$c}){item{id}}}
""", p=project["id"], c=issue["node_id"])
            item_id = result["addProjectV2ItemById"]["item"]["id"]
            items[issue["node_id"]] = item_id
        gql("""
mutation($p:ID!,$i:ID!,$f:ID!,$o:String!){
 updateProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,fieldId:$f,
 value:{singleSelectOptionId:$o}}){projectV2Item{id}}}
""", p=project["id"], i=item_id, f=status_field["id"], o=options[task["status"]])
        state["issues"][task_id] = {
            "number": issue["number"], "url": issue["html_url"], "node_id": issue["node_id"],
            "item_id": item_id, "status": task["status"], "milestone": task["milestone_key"]}
        save(state)
        print(f"{task_id}: issue #{issue['number']} -> {task['status']}", flush=True)
    fields = api(PROJECT_PATH + "/fields")
    ids = {field["name"]: field["id"] for field in fields}
    existing = next((v for v in project["views"]["nodes"]
                     if v["name"] == "All Tasks" and v["layout"] == "TABLE_LAYOUT"), None)
    if existing is None:
        response = api(PROJECT_PATH + "/views", "POST", {
            "name": "All Tasks", "layout": "table", "filter": "is:issue",
            "visible_fields": [ids[name] for name in PLAN["table_view"]["visible_fields"]],
            "sort_by": [[ids["Title"], "asc"]]
        })
        view = response.get("value", response)
        state["views"].append(view)
        save(state)
        print("Created All Tasks table view.", flush=True)
    gql("""
mutation($p:ID!,$r:ID!){linkProjectV2ToRepository(input:{projectId:$p,repositoryId:$r}){clientMutationId}}
""", p=project["id"], r=data["repository"]["id"])
    state["status"] = "project_items_published_docs_pending"
    save(state)
    with (ROOT / "planning/backlog.csv").open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream)
        columns, tasks = reader.fieldnames, list(reader)
    for task in tasks:
        task["github_issue_url"] = state["issues"][task["id"]]["url"]
        task["notes"] = "Published in Project #1; current ownership is tracked in planning/team.json and the backlog."
    with (ROOT / "planning/backlog.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(tasks)
    print("Published 4 milestones and 20 Project issues; assignees unchanged.", flush=True)


if __name__ == "__main__":
    main()
