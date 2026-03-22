from pathlib import Path


def next_revision(job_dir: Path, base_stem: str) -> int:
    pattern = f"{base_stem}_r"
    revisions = []
    for candidate in job_dir.glob(f"{base_stem}_r*.json"):
        name = candidate.stem
        if pattern in name:
            tail = name.split("_r")[-1]
            if tail.isdigit():
                revisions.append(int(tail))
    return (max(revisions) + 1) if revisions else 1


def revision_tag(rev: int) -> str:
    return f"r{rev:03d}"
