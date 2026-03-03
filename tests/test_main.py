from app import main
from tempfile import TemporaryDirectory
from pathlib import Path
import pytest


@pytest.mark.parametrize(
    ["data", "is_ext", "expected_file_name"],
    [pytest.param({".pug-lintrc": "pug"}, False, ".pug-lintrc")],
)
def test_create_file(data, is_ext, expected_file_name):
    with TemporaryDirectory() as dir:
        current = Path(dir)
        main.create_file(data, is_ext, False, current)

        result_files = list(current.iterdir())
        assert result_files[0].name == expected_file_name
