"""Build a self-contained GitHub Wiki bundle; no network or Git mutations."""
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/wiki"
OUTPUT = ROOT / "dist/wiki"


def convert_links(text, summary=False):
    def convert(match):
        label, target = match.groups()
        if target.startswith(("https://", "http://", "#", "mailto:")):
            return match.group(0)
        path, sep, anchor = target.partition("#")
        if path in ("../research/survey-summary.md", "survey-summary.md"):
            path = "Survey-Summary"
        elif path in ("../research/survey-summary.json", "survey-summary.json"):
            path = "Survey-Aggregates"
        elif summary and path.startswith("../wiki/"):
            path = path.removeprefix("../wiki/").removesuffix(".md")
        elif "/" not in path and path.endswith(".md"):
            path = path.removesuffix(".md")
        return f"[{label}]({path}{sep}{anchor})"
    return re.sub(r"\[([^\]]+)\]\(([^)\n]+)\)", convert, text)


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    pages = sorted(SOURCE.glob("*.md"))
    for page in pages:
        (OUTPUT / page.name).write_text(convert_links(page.read_text(encoding="utf-8")), encoding="utf-8")
    summary = (ROOT / "docs/research/survey-summary.md").read_text(encoding="utf-8")
    (OUTPUT / "Survey-Summary.md").write_text(convert_links(summary, summary=True), encoding="utf-8")
    aggregate = (ROOT / "docs/research/survey-summary.json").read_text(encoding="utf-8")
    (OUTPUT / "Survey-Aggregates.md").write_text(
        "# Survey aggregate data\n\nAggregate only; no respondent-level rows or contacts.\n\n"
        "~~~json\n" + aggregate.rstrip() + "\n~~~\n", encoding="utf-8"
    )
    sidebar = ["[Home](Home)", ""]
    sidebar.extend(f"- [{page.stem.replace('-', ' ')}]({page.stem})" for page in pages if page.stem != "Home")
    sidebar.extend(["", "- [Survey summary](Survey-Summary)", "- [Survey aggregate](Survey-Aggregates)", ""])
    (OUTPUT / "_Sidebar.md").write_text("\n".join(sidebar), encoding="utf-8")
    (OUTPUT / "_Footer.md").write_text(
        "[Home](Home) · [Evidence](16-Evidence-Register) · [Submission status](15-Submission-Checklist)\n",
        encoding="utf-8"
    )
    archive = OUTPUT.parent / "LockIn-Assignment1-Wiki.zip"
    with ZipFile(archive, "w", compression=ZIP_DEFLATED) as bundle:
        for page in sorted(OUTPUT.glob("*.md")):
            bundle.write(page, arcname=page.name)
    print(f"Exported {len(pages) + 4} Markdown pages to {OUTPUT}")
    print(f"Prepared Wiki bundle: {archive}")
    print("Export writes local files only; this command does not update the live Wiki or Project.")


if __name__ == "__main__":
    main()
