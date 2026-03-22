from .constants import RECENT_JOBS_LIMIT
from .state import load_state, save_state


def push_recent_job(context, job_path: str) -> None:
    state = load_state(context)
    jobs = [item for item in state.get("recent_jobs", []) if item != job_path]
    jobs.insert(0, job_path)
    state["recent_jobs"] = jobs[:RECENT_JOBS_LIMIT]
    save_state(context, state)


def list_recent_jobs(context):
    return load_state(context).get("recent_jobs", [])
