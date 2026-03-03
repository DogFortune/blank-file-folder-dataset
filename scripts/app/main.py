import json
import argparse
from pathlib import Path


def load_json(path: str):
    with open(path) as f:
        raw_json = json.load(f)

    return raw_json


def create_file(
    file_data: dict, is_ext: bool, verbose: bool, current: Path = Path("files")
):
    """ファイルを作成します

    :param file_data: テーマから抽出したファイル情報
    :type file_data: dict
    :param is_ext: 拡張子用のファイルか否か
    :type is_ext: bool
    :param verbose: 詳細表示か否か
    :type verbose: bool
    """
    if not current.is_dir():
        current.mkdir()
    for key, value in file_data.items():
        file_path = (
            current.joinpath(f"{value}.{key}") if is_ext else current.joinpath(key)
        )
        if file_path.is_file():
            if verbose:
                print(f"skip: {str(file_path)}")
            continue
        else:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.touch()
            print(f"create: {str(file_path)}")


def create_folder(folder_data: dict, verbose: bool):
    """フォルダを作成します。フォルダだけだとgit管理に含まれないのでからのファイルをフォルダ内に作っておきます。

    :param folder_info_json: _description_
    :type folder_info_json: dict
    :param verbose: 詳細表示か否か
    :type verbose: bool
    """
    current = Path("folders")
    if not current.is_dir():
        current.mkdir()
    for folder_name in folder_data.keys():
        folder_path = current.joinpath(folder_name)
        if folder_path.is_dir():
            if verbose:
                print(f"skip: {str(folder_path)}")
            continue
        else:
            folder_path.mkdir(parents=True)
            with open(folder_path.joinpath("empty.txt"), "w") as f:
                f.write("")
                print(f"create: {folder_path}")


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def main(args=None):
    parser = create_parser()
    args = parser.parse_args(args)

    verbose = args.verbose

    file_data = load_json("./manifests/files.json")
    create_file(file_data, False, verbose)

    ext_data = load_json("./manifests/extensions.json")
    create_file(ext_data, True, verbose)

    folder_data = load_json("./manifests/folders.json")
    create_folder(folder_data, verbose)


if __name__ == "__main__":
    main()
