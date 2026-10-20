"""Read-only GitHub checks against the current backlog; writes a local verification record."""
from collections import Counter
import csv
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import urllib.request
from publish_github_project import gql

ROOT = Path(__file__).resolve().parents[1]


def main():
    with (ROOT / "planning/backlog.csv").open(encoding="utf-8", newline="") as stream:
        tasks = list(csv.DictReader(stream))
    state = json.loads((ROOT / "planning/github/published-state.json").read_text(encoding="utf-8"))
    result = gql("""
query { organization(login:"Lockin-4everyung"){projectV2(number:1){
 public views(first:20){nodes{number name layout}}
 items(first:100){totalCount nodes{
  fieldValueByName(name:"Status"){... on ProjectV2ItemFieldSingleSelectValue{name}}
  content{... on Issue{number title milestone{title} assignees(first:10){nodes{login}}}}
 }}
}}}
""")["organization"]["projectV2"]
    items = result["items"]["nodes"]
    assert result["public"] and result["items"]["totalCount"] == len(tasks)
    by_number = {item["content"]["number"]: item for item in items}
    counts = Counter(item["fieldValueByName"]["name"] for item in items)
    assigned = 0
    for task in tasks:
        issue = by_number[state["issues"][task["id"]]["number"]]
        expected = ({task["github_assignee"]} if task["github_assignee"] else set())
        expected.update(filter(None, task.get("github_support", "").split(";")))
        actual = {person["login"] for person in issue["content"]["assignees"]["nodes"]}
        assert actual == expected, f"Assignee mismatch for {task['id']}: {actual} != {expected}"
        expected_status = "In Review" if task["status"] == "Review" else task["status"]
        assert issue["fieldValueByName"]["name"] == expected_status
        assert issue["content"]["milestone"]["title"].startswith(task["milestone"] + " - ")
        assigned += bool(actual)
    assert any(view["name"] == "All Tasks" and view["layout"] == "TABLE_LAYOUT" for view in result["views"]["nodes"])
    urls = [
        "https://github.com/Lockin-4everyung/lockin-mobile",
        "https://github.com/Lockin-4everyung/lockin-mobile/wiki",
        "https://github.com/Lockin-4everyung/lockin-mobile/wiki/13-Project-Foundation-Plan",
        "https://github.com/Lockin-4everyung/lockin-mobile/wiki/14-Traceability-Matrix",
        "https://github.com/Lockin-4everyung/lockin-mobile/wiki/11-Critical-User-Flows",
        "https://github.com/Lockin-4everyung/lockin-mobile/wiki/Survey-Summary",
        "https://github.com/orgs/Lockin-4everyung/projects/1/views/1",
        "https://github.com/orgs/Lockin-4everyung/projects/1/views/2",
        "https://raw.githubusercontent.com/Lockin-4everyung/lockin-mobile/main/docs/research/survey-summary.json",
    ]
    checked = []
    for url in urls:
        request = urllib.request.Request(url, headers={"User-Agent": "LockIn-Documentation-Verification"})
        with urllib.request.urlopen(request, timeout=30) as response:
            content = response.read()
            assert response.status == 200 and content
            if "raw.githubusercontent" in url:
                assert json.loads(content)["source"]["n"] == 12
            checked.append({"url": url, "http_status": response.status, "authenticated": False})
        print("Public HTTP 200:", url, flush=True)
    verified_on = datetime.now(timezone(timedelta(hours=7))).date().isoformat()
    verification = {
        "verified_on": verified_on, "public": True, "items": len(items),
        "status_counts": dict(counts), "milestones": len(state["milestones"]),
        "assigned_tasks": assigned, "unassigned_tasks": len(items) - assigned,
        "views": result["views"]["nodes"], "public_links": checked,
        "figma_access": "User-provided link; design contents not reviewed by this checker.",
        "submission": "No course submission performed by this checker."
    }
    (ROOT / "planning/github/verification.json").write_text(
        json.dumps(verification, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"PASS: {len(items)} issues, {assigned} assigned, {len(items)-assigned} unassigned; no GitHub mutations.", flush=True)


if __name__ == "__main__":
    main()
