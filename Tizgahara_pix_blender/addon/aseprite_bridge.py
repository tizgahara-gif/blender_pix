import subprocess
from pathlib import Path


def launch_aseprite(aseprite_executable: str, job_file: Path) -> subprocess.CompletedProcess:
    cmd = [aseprite_executable, str(job_file)]
    return subprocess.run(cmd, check=False, capture_output=True, text=True)
