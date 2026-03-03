from app import main
from tempfile import TemporaryDirectory
from pathlib import Path


def test_create_file():
    file_data = {
        ".pug-lintrc": "pug",
        ".pug-lintrc.js": "pug",
        ".pug-lintrc.json": "pug",
        "justfile": "just",
        ".justfile": "just",
    }
    with TemporaryDirectory() as dir:
        current = Path(dir)
        main.create_file(file_data, False, False, current)

        assert len(list(current.iterdir())) == 5
