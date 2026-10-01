# TODO: Setting file paths for pathlib

from pathlib import Path

DEFAULT_DIR = Path.home() / "Music"


class Filesystem:
    def __init__(self, path: str | Path) -> None:
        self.path: Path = Path(path).expanduser()

    def create_directory(self):
        dir = self.path.mkdir(parents=True, exist_ok=True)
        return f"{dir} is created"

    def save_location(self):
        if DEFAULT_DIR.is_dir():
            return DEFAULT_DIR

        else:
            print(self.create_directory())

        return self.path
