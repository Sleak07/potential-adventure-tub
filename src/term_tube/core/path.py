# TODO: Setting file paths for pathlib

from pathlib import Path


def get_ssh_dir() -> Path:
    """Return the current user's ~/.ssh directory."""
    return Path.home() / ".ssh"
