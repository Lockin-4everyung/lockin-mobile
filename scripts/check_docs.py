"""Check local links, traceability, task dependencies and survey aggregate consistency."""
from collections import Counter
import csv
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []
CHECKS = 0


def require(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)


def headings(text):
    return {
        re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-")
        for h in re.findall(r"^#{1,6}\s+(.+)$", text, re.M)
    }


def check_links(folder, wiki_export=False):
    paths = [p for p in folder.rglob("*.md") if not any(
        part in (".git", ".cache", "node_modules", "dist")
        for part in p.relative_to(folder).parts)]
    local_count, diagrams = 0, 0
    for file in paths:
        text = file.read_text(encoding="utf-8")
        fences = re.findall(r"^(?:\x60{3}|~{3}).*$", text, re.M)
        require(len(fences) % 2 == 0, f"Unclosed fence: {file}")
        diagrams += len(re.findall(r"^(?:\x60{3}|~{3})mermaid\s*$", text, re.M))
        for _, raw in re.findall(r"\[([^\]]+)\]\(([^)\n]+)\)", text):
            target = unquote(raw.strip().strip("<>"))
            parsed = urlsplit(target)
            if parsed.scheme in ("http", "https", "mailto"):
                continue
            require(not parsed.scheme, f"Unexpected link scheme: {file}: {raw}")
            path_part, _, anchor = target.partition("#")
            dest = (file.parent / path_part).resolve() if path_part else file
            if wiki_export and not dest.exists():
                dest = Path(str(dest) + ".md")
            local_count += 1
            require(dest.is_file(), f"Broken link: {file.relative_to(folder)} -> {raw}")
            if anchor and dest.is_file() and dest.suffix == ".md":
                require(anchor in headings(dest.read_text(encoding="utf-8")), f"Missing anchor: {raw}")
    return local_count, diagrams


def check_traceability():
    wiki = ROOT / "docs/wiki"
    stories = (wiki / "10-User-Stories.md").read_text(encoding="utf-8")
    matrix = (wiki / "14-Traceability-Matrix.md").read_text(encoding="utf-8")
    scope = (wiki / "09-MVP-Scope-Impact-Effort.md").read_text(encoding="utf-8")
    flows = (wiki / "11-Critical-User-Flows.md").read_text(encoding="utf-8")
    plan = (wiki / "13-Project-Foundation-Plan.md").read_text(encoding="utf-8")
    with (ROOT / "planning/backlog.csv").open(encoding="utf-8", newline="") as stream:
        tasks = list(csv.DictReader(stream))
    team = json.loads((ROOT / "planning/team.json").read_text(encoding="utf-8"))
    members = {member["github"] for member in team["members"]}
    ids = {t["id"] for t in tasks}
    require(len(ids) == len(tasks) == 20, "Expected 20 unique backlog tasks.")
    for task in tasks:
        task_id = task["id"]
        require(task["status"] in {"Backlog", "To Do", "In Progress", "Review", "Done"}, f"Unknown status: {task_id}")
        require(task["owner_role"] and task["acceptance_criteria"], f"Missing role/acceptance: {task_id}")
        match = re.search(r"^\| " + re.escape(task_id) + r" \|.*$", plan, re.M)
        require(match and f"| {task['status']} |" in match.group(0), f"Plan/CSV status mismatch: {task_id}")
        assigned = [task["github_assignee"]] if task["github_assignee"] else []
        assigned += list(filter(None, task.get("github_support", "").split(";")))
        require(all(user in members for user in assigned), f"Unknown team member assigned to {task_id}")
        if task_id in team["unassigned_tasks"]:
            require(not assigned, f"Owner not yet specified for {task_id}")
        if task["github_issue_url"]:
            require(re.fullmatch(r"https://github\.com/Lockin-4everyung/lockin-mobile/issues/\d+", task["github_issue_url"]), f"Invalid published issue URL: {task_id}")
        for dep in filter(None, task["depends_on"].split(";")):
            require(dep in ids, f"Unknown dependency {dep} in {task_id}")
    graph = {t["id"]: list(filter(None, t["depends_on"].split(";"))) for t in tasks}
    visiting, visited = set(), set()
    def visit(task_id):
        if task_id in visiting:
            require(False, f"Dependency cycle at {task_id}")
            return
        if task_id in visited:
            return
        visiting.add(task_id)
        for dep in graph.get(task_id, []):
            visit(dep)
        visiting.remove(task_id)
        visited.add(task_id)
    for task_id in graph:
        visit(task_id)
    for n in range(1, 11):
        story = f"US-{n:02}"
        require(story in stories and story in matrix, f"Untraced story: {story}")
        require(any(story in t["stories"].split(";") for t in tasks), f"No task for {story}")
    for n in range(1, 9):
        feature = f"F-{n:02}"
        require(feature in scope and feature in matrix, f"Untraced feature: {feature}")
        require(any(feature in t["features"].split(";") for t in tasks), f"No task for {feature}")
        require(f"R-{n:02}" in matrix and f"E-{n:02}" in matrix, f"Missing requirement/evidence {n}")
    for flow in ("FL-01", "FL-02"):
        require(flow in flows and flow in matrix, f"Untraced flow: {flow}")
    decisions = (wiki / "07-Evidence-Evaluation-Product-Decisions.md").read_text(encoding="utf-8")
    for n in range(1, 9):
        require(re.search(rf"\bA{n}(?:/H1)?:", decisions), f"Missing assumption decision A{n}")
    print("Task statuses:", dict(Counter(t["status"] for t in tasks)))


def check_survey():
    data = json.loads((ROOT / "docs/research/survey-summary.json").read_text(encoding="utf-8"))
    n, counts, derived = data["source"]["n"], data["counts"], data["derived"]
    require(n == 12, "Update sample descriptions if N changes.")
    for key in ("screening_student", "screening_recent_self_study", "Q1_year", "Q3_recent_session",
                "Q6_friend_appointments", "Q7_last_group_session", "Q8_accountability",
                "Q10_commitment_rating", "Q11_value", "Q12_different_rooms",
                "Q15_public_room_rating", "Q19_preferred_alternative", "Q20_install_intention"):
        require(sum(counts[key].values()) == n, f"Inconsistent single-select count: {key}")
    for key in ("Q7_last_group_session", "Q8_accountability"):
        require(counts[key]["(Không trả lời)"] == 4, f"Branching denominator changed: {key}")
    require(derived["Q21_planned_sessions"] == 52 and derived["Q22_reported_mostly_completed_sessions"] == 36,
            "Totals differ from verified source.")
    weighted = sum(int(key) * value for key, value in counts["Q10_commitment_rating"].items())
    require(abs(weighted / n - derived["Q10_mean"]) < 1e-9, "Q10 mean inconsistent.")
    require(derived["Q21_Q22_people_below_plan"] == 9, "Below-plan count inconsistent.")
    require("rows" not in data and "respondents" not in data and "contact" not in counts, "Raw research in aggregate.")


def main():
    links, diagrams = check_links(ROOT)
    flow_text = (ROOT / "docs/wiki/11-Critical-User-Flows.md").read_text(encoding="utf-8")
    flow_diagrams = len(re.findall(r"^(?:\x60{3}|~{3})mermaid\s*$", flow_text, re.M))
    require(flow_diagrams == 2, f"Expected two critical user flows, got {flow_diagrams}.")
    check_traceability()
    check_survey()
    exported_links = 0
    if (ROOT / "dist/wiki").exists():
        exported_links, exported_diagrams = check_links(ROOT / "dist/wiki", wiki_export=True)
        require(exported_diagrams == diagrams, "Source/Wiki Mermaid block counts differ.")
    for error in ERRORS:
        print("ERROR:", error)
    print(f"{CHECKS} checks; {links} source links; {exported_links} exported links; {diagrams} Mermaid blocks.")
    print("Mermaid syntax needs a Mermaid engine; block count alone is not a parser test.")
    print("External links, live GitHub access and actual user research are outside this local checker.")
    if ERRORS:
        return 1
    print("PASS: links, traceability, task graph and aggregate consistency.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
