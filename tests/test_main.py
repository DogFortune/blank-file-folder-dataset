from app import main
from tempfile import TemporaryDirectory
from pathlib import Path
import pytest


@pytest.mark.parametrize(
    ["data", "is_ext", "expected_file_name"],
    [
        pytest.param({".pug-lintrc": "pug"}, False, ".pug-lintrc"),
        pytest.param({"png": "image"}, True, "image.png"),
        pytest.param({"key": "value"}, True, "value.key"),
    ],
)
def test_create_file(data, is_ext, expected_file_name):
    """渡したデータから、想定している名前のファイルが生成されている事
    file.json -> ファイル名は{key}になる事
    extensions.json -> ファイル名は{value}.{key}になる事

    :param data: _description_
    :type data: _type_
    :param is_ext: _description_
    :type is_ext: bool
    :param expected_file_name: _description_
    :type expected_file_name: _type_
    """
    with TemporaryDirectory() as dir:
        current = Path(dir)
        main.create_file(data, is_ext, False, current)

        result_file = list(current.iterdir())

        assert len(result_file) == 1
        assert result_file[0].name == expected_file_name


@pytest.mark.parametrize(
    ["data", "expected_folder_name"],
    [
        pytest.param({"rust": "folder-rust"}, "rust"),
    ],
)
def test_create_folder(data, expected_folder_name):
    with TemporaryDirectory() as dir:
        current = Path(dir)
        main.create_folder(data, False, current)

        result_folder = list(current.iterdir())
        assert len(result_folder) == 1
        assert result_folder[0].name == expected_folder_name
