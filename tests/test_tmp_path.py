# TODO: Test for temp directory and file using pytest
from pathlib import Path

import pytest

from term_tube.core.path import get_ssh_dir


def test_get_ssh_dir(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(Path, "home", lambda: tmp_path)

    assert get_ssh_dir() == tmp_path / ".ssh"
