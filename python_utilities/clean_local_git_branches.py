import subprocess
import os
import sys


def fetch_branches(dir):
    """Return local branch names from the current git repository."""
    try:
        os.chdir(dir)
        result = subprocess.run(
            ["git", "branch", "--format=%(refname:short)"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []

    return [line.strip() for line in result.stdout.splitlines() if line.strip()]

directory = sys.argv[1]
print("provided directory: ", directory)

for branch in fetch_branches(directory):
    print(f"deleting: {branch}\n")
    try:
        result = subprocess.run(
            ["git", "branch", "-d", branch],
            capture_output=True,
            text=True,
            check=True,
        )
        print(f"deleted successfully: {branch}")
    except FileNotFoundError as err:
        print(f"failed to delete {branch}: git not found ({err})")
    except subprocess.CalledProcessError as err:
        error_msg = (err.stderr or err.stdout or "").strip()
        if error_msg:
            print(f"failed to delete {branch}: {error_msg}")
        else:
            print(f"failed to delete {branch}: git command returned exit code {err.returncode}")