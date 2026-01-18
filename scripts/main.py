import json
from pathlib import Path


def __load_json(path: str):
    with open(path) as f:
        raw_json = json.load(f)

    return raw_json


def create_file(file_data: dict, is_ext: bool):
    """ファイルを作成します

    :param file_data: テーマから抽出したファイル情報
    :type file_data: dict
    :param is_ext: 拡張子用のファイルか否か
    :type is_ext: bool
    """
    current = Path("files")
    if not current.is_dir():
        current.mkdir()
    for key in file_data.keys():
        file_path = (
            current.joinpath(f"DummyName.{key}") if is_ext else current.joinpath(key)
        )
        if file_path.is_file():
            print(f"skip: {str(file_path)}")
            continue
        else:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.touch()
            print(f"create: {str(file_path)}")


def create_folder(folder_data: dict):
    """フォルダを作成します。フォルダだけだとgit管理に含まれないのでからのファイルをフォルダ内に作っておきます。

    :param folder_info_json: _description_
    :type folder_info_json: dict
    """
    current = Path("folders")
    if not current.is_dir():
        current.mkdir()
    for folder_name in folder_data.keys():
        folder_path = current.joinpath(folder_name)
        if folder_path.is_dir():
            print(f"skip: {str(folder_path)}")
            continue
        else:
            folder_path.mkdir(parents=True)
            with open(folder_path.joinpath("empty.txt"), "w") as f:
                f.write("")
                print(f"create: {folder_path}")


def main():
    file_data = __load_json("./files.json")
    create_file(file_data, False)

    ext_data = __load_json("./extensions.json")
    create_file(ext_data, True)

    folder_data = __load_json("./folders.json")
    create_folder(folder_data)


if __name__ == "__main__":
    main()
