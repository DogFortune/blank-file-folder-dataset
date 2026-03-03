from app import main


def test_create_file():
    file_data = main.load_json("./manifests/files.json")
    print(file_data)
