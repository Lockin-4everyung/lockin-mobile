"""Finish Project publication and verify public entry points without authentication."""
from collections import Counter
import json
from pathlib import Path
import urllib.request
from publish_github_project import api, gql

ROOT = Path(__file__).resolve().parents[1]
STATE = json.loads((ROOT / "planning/github/published-state.json").read_text(encoding="utf-8"))
PROJECT_ID = STATE["project_id"]

def main():
    data = gql("""
query { organization(login:"Lockin-4everyung"){projectV2(number:1){
 id readme
 fields(first:30){nodes{... on ProjectV2SingleSelectField{id name options{id name}}}}
}}}
""")
    project_before = data["organization"]["projectV2"]
    assert project_before["id"] == PROJECT_ID
    fields = project_before["fields"]["nodes"]
    status = next(f for f in fields if f.get("name") == "Status")
    review_id = next(o["id"] for o in status["options"] if o["name"] == "In Review")
    gql("""
mutation($p:ID!,$i:ID!,$f:ID!,$o:String!){
 updateProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,fieldId:$f,value:{singleSelectOptionId:$o}}){projectV2Item{id}}
}
""", p=PROJECT_ID, i=STATE["issues"]["T-17"]["item_id"], f=status["id"], o=review_id)
    # Re-read and merge two publication lines; preserve all criteria and user edits.
    issue = api("repos/Lockin-4everyung/lockin-mobile/issues/17")
    assert issue["title"].startswith("[T-17]")
    issue_body = issue["body"] or ""
    issue_body = issue_body.replace("Status đề xuất: Backlog", "Status hiện tại: In Review", 1)
    old_note = "Công việc dự kiến, chưa thực hiện. Không coi template/protocol là kết quả nghiên cứu hoặc implementation."
    new_note = "Đã xuất bản source repository, Wiki và 20 issue/4 milestone; Board/Table có thể truy cập public. Chờ nhóm review. Assignee để trống theo yêu cầu người dùng; chưa đánh dấu Done."
    if old_note in issue_body:
        issue_body = issue_body.replace(old_note, new_note, 1)
    elif new_note not in issue_body:
        issue_body += "\n\n## Publication update - 19/10/2026\n\n" + new_note + "\n"
    api("repos/Lockin-4everyung/lockin-mobile/issues/17", "PATCH", {"body": issue_body})
    (ROOT / "planning/github/issues/T-17.md").write_text(issue_body, encoding="utf-8")
    readme = """# LockIn - Product Development

Theo dõi nghiên cứu người dùng, quyết định sản phẩm, thiết kế, phát triển và kiểm thử MVP LockIn.

- [Public entry / repository](https://github.com/Lockin-4everyung/lockin-mobile)
- [Assignment 1 Wiki](https://github.com/Lockin-4everyung/lockin-mobile/wiki)
- [Project plan](https://github.com/Lockin-4everyung/lockin-mobile/wiki/13-Project-Foundation-Plan)
- [Evidence and traceability](https://github.com/Lockin-4everyung/lockin-mobile/wiki/14-Traceability-Matrix)
- [Anonymous survey aggregate](https://github.com/Lockin-4everyung/lockin-mobile/wiki/Survey-Summary)
- [All Tasks table](https://github.com/orgs/Lockin-4everyung/projects/1/views/2)

## Milestones

M1 - Assignment 1 Foundation; M2 - Discovery Follow-up and Design; M3 - Core Mobile MVP; M4 - Pilot and Product Decision.

## Workflow and progress

Backlog -> Todo -> In Progress -> In Review -> Done.

Snapshot 19/10/2026: 20 issues; 5 In Review; 15 Backlog; 0 Done. Assignees are intentionally unset at the user's request. Actual work is tracked by the items and their milestones. Planned research/build work has not been marked complete.

Move an item to In Review when its artifact exists. Move to Done only after acceptance and review. No course submission has been performed.
"""
    # This is Project #1's README, not repository README.md. Preserve any existing text.
    existing_readme = project_before["readme"] or ""
    marker = "<!-- lockin-publication-snapshot-2026-10-19 -->"
    if marker not in existing_readme:
        readme = existing_readme.rstrip() + ("\n\n" if existing_readme else "") + marker + "\n" + readme
    else:
        readme = existing_readme
    gql("""
mutation($p:ID!,$body:String!){updateProjectV2(input:{projectId:$p,readme:$body}){projectV2{id}}}
""", p=PROJECT_ID, body=readme)
    result = gql("""
query { organization(login:"Lockin-4everyung"){projectV2(number:1){
 public views(first:20){nodes{number name layout}}
 items(first:100){totalCount nodes{
  fieldValueByName(name:"Status"){... on ProjectV2ItemFieldSingleSelectValue{name}}
  content{... on Issue{number title milestone{title} assignees(first:10){totalCount}}}
 }}
}}}
""")["organization"]["projectV2"]
    items = result["items"]["nodes"]
    counts = Counter(item["fieldValueByName"]["name"] for item in items)
    assert result["public"] and len(items) == result["items"]["totalCount"] == 20
    assert counts == {"In Review": 5, "Backlog": 15}
    assert all(item["content"]["assignees"]["totalCount"] == 0 for item in items)
    assert all(item["content"]["milestone"] for item in items)
    assert any(v["name"] == "All Tasks" and v["layout"] == "TABLE_LAYOUT" for v in result["views"]["nodes"])
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
            status_code = response.status
            content = response.read()
            assert status_code == 200 and content
            if "raw.githubusercontent" in url:
                assert json.loads(content)["source"]["n"] == 12
            checked.append({"url": url, "http_status": status_code, "authenticated": False})
        print("Public HTTP 200:", url, flush=True)
    verification = {
        "verified_on": "2026-10-19", "public": result["public"], "items": len(items),
        "status_counts": dict(counts), "milestones": 4, "unassigned": 20,
        "views": result["views"]["nodes"], "public_links": checked,
        "mermaid": "Both flowchart-v2 definitions parsed successfully; live visual review remains a team review task.",
        "submission": "Not submitted to course portal."
    }
    (ROOT / "planning/github/verification.json").write_text(
        json.dumps(verification, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print("PASS: 20 issues, 4 milestones, 5 In Review, 15 Backlog, no assignees, public links.", flush=True)

if __name__ == "__main__":
    main()
