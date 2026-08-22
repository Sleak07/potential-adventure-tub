# Handling file process

from abc import ABC, abstractmethod
from pathlib import Path
from typing import override


class Filesystem(ABC):
    def __init__(self, directory: str | Path, missing_dir: bool = True) -> None:
        self.directory: Path = Path(directory).resolve()

        match self.directory.exists(), missing_dir:
            case True, _:
                pass
            case False, True:
                self.directory.mkdir(parents=True, exist_ok=True)
            case False, False:
                raise FileNotFoundError(f"Directory not found: {self.directory}")

    # checks the correct file
    @abstractmethod
    def find_correct_files(self) -> list[Path]:

        pass

    def is_valid_directory(self) -> bool:
        return self.directory.exists() and self.directory.is_dir()

    @override
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(directory={self.directory!r})"
