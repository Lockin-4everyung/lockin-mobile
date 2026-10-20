"""Prepare exact milestone and issue bodies for Project #1 without changing GitHub."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "planning/github"
ORG = "Lockin-4everyung"
REPO = "lockin-mobile"
PROJECT = "https://github.com/orgs/Lockin-4everyung/projects/1/views/1"
SOURCE = f"https://github.com/{ORG}/{REPO}/blob/main/docs/wiki"

PAGE_MAP = {
    "Research": "05-User-Market-Research.md",
    "Product": "09-MVP-Scope-Impact-Effort.md",
    "Design": "11-Critical-User-Flows.md",
    "Mobile": "11-Critical-User-Flows.md",
    "Data": "17-Product-Rules-Metrics.md",
    "QA": "11-Critical-User-Flows.md",
    "Coordinator": "13-Project-Foundation-Plan.md",
}
MILESTONES = [
    ("M1", "M1 - Assignment 1 Foundation",
     "Tài liệu được review; Wiki và Project public; kiểm tra evidence/links. Phân công thành viên sẽ bổ sung sau theo yêu cầu người dùng."),
    ("M2", "M2 - Discovery Follow-up and Design",
     "Nghiên cứu tiếp theo protocol, so sánh baseline/prototype, cập nhật quyết định và chốt scope/capacity."),
    ("M3", "M3 - Core Mobile MVP",
     "Luồng tạo hẹn, mời, RSVP, reminder, check-in, outcome hoạt động; kiểm thử quyền, offline, retry và timezone."),
    ("M4", "M4 - Pilot and Product Decision",
     "Chạy pilot khi có consent và mẫu phù hợp; ghi dữ liệu thiếu; đánh giá H1 và quyết định Keep/Revise/Reject/Investigate further."),
]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    issue_dir = OUT / "issues"
    milestone_dir = OUT / "milestones"
    issue_dir.mkdir(exist_ok=True)
    milestone_dir.mkdir(exist_ok=True)
    with (ROOT / "planning/backlog.csv").open(encoding="utf-8", newline="") as stream:
        tasks = list(csv.DictReader(stream))
    manifest = {
        "organization": ORG, "repository": REPO, "project_number": 1,
        "project_url": PROJECT, "checked_public_on": "2026-10-19",
        "publication_status": "prepared_local_not_published",
        "assignment_source": "planning/team.json; user-confirmed 2026-10-20; implementation/software QA pending",
        "status_mapping": {"Backlog": "Backlog", "To Do": "Todo", "In Progress": "In Progress", "Review": "In Review", "Done": "Done"},
        "milestones": [], "issues": [],
        "table_view": {"name": "All Tasks", "layout": "table",
                       "visible_fields": ["Title", "Assignees", "Status", "Milestone"]},
        "dates": "No due dates supplied; leave unset.",
    }
    for key, title, desc in MILESTONES:
        payload = {"title": title, "description": desc}
        (milestone_dir / f"{key}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        manifest["milestones"].append({"key": key, **payload})
    for task in tasks:
        task_id = task["id"]
        primary = task.get("github_assignee", "")
        support = list(filter(None, task.get("github_support", "").split(";")))
        assignees = ([primary] if primary else []) + support
        criteria = [part.strip() for part in task["acceptance_criteria"].split(";") if part.strip()]
        body = [
            f"## Mục tiêu\n\n{task['title']}.",
            f"## Theo dõi\n\n- Task ID: {task_id}\n- Milestone: {task['milestone']}\n"
            f"- Status đề xuất: {manifest['status_mapping'][task['status']]}\n"
            f"- Chủ trì: {primary or 'Chưa phân công'}\n- Hỗ trợ: {', '.join(support) or '-'}",
            "## Traceability\n\n"
            f"- Evidence / hypothesis / assignment requirement: {task['evidence_or_requirement'] or 'Project foundation'}\n"
            f"- User stories: {task['stories'] or 'Không áp dụng cho research/foundation task'}\n"
            f"- MVP features: {task['features'] or 'Không áp dụng'}\n"
            f"- User flows: {task['flows'] or 'Không áp dụng'}",
            "## Acceptance criteria\n\n" + "\n".join("- [ ] " + value for value in criteria),
            "## Dependencies\n\n" + (task["depends_on"].replace(";", ", ") or "Không có dependency trước."),
            "## Tài liệu liên quan\n\n"
            f"- [Project plan]({SOURCE}/13-Project-Foundation-Plan.md)\n"
            f"- [Traceability matrix]({SOURCE}/14-Traceability-Matrix.md)\n"
            f"- [Chi tiết]({SOURCE}/{PAGE_MAP[task['owner_role']]})\n"
            f"- [GitHub Project]({PROJECT})",
            "## Trạng thái bằng chứng\n\n" + (
                "Đã chuẩn bị artifact local; chờ nhóm review/chốt. Chưa coi là Done, chưa có team sign-off."
                if task["status"] == "Review" else
                "Công việc dự kiến, chưa thực hiện. Không coi template/protocol là kết quả nghiên cứu hoặc implementation."
            ),
        ]
        text = "\n\n".join(body) + "\n"
        if chr(0x2014) in text:
            raise ValueError("Em-dash is not allowed.")
        (issue_dir / f"{task_id}.md").write_text(text, encoding="utf-8")
        manifest["issues"].append({
            "task_id": task_id, "title": f"[{task_id}] {task['title']}",
            "milestone_key": task["milestone"], "status": manifest["status_mapping"][task["status"]],
            "body_file": f"issues/{task_id}.md", "assignees": assignees
        })
    (OUT / "publication-plan.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Prepared {len(MILESTONES)} milestone payloads and {len(tasks)} issue bodies.")
    print("No GitHub objects were created; assignments follow the backlog, and due dates remain unset.")

if __name__ == "__main__":
    main()
