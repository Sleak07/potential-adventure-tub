# TODO: Setting file paths for pathlib

from pathlib import Path


class Filesystem:
    def __init__(self, path: str | Path) -> None:
        self.path: Path = Path(path).expanduser()
        self.path.mkdir(parents=True, exist_ok=True)

        self.config_file: Path = self.path / "config,txt"
        self.config_file.touch(exist_ok=True)

    def read_config_file(self):
        return self.config_file.read_text().splitlines()


file_system = Filesystem("~/dev/Python/term-tube/")
print(file_system.read_config_file())


# setting the default config path
