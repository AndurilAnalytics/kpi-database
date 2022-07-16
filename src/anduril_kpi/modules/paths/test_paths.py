import pathlib

from ..paths import path

def test_path_creation():
    folder = 'test/'
    folder_path = pathlib.Path(folder)
    file_name = 'test_file.csv'
    test_path = folder_path.joinpath(file_name)

    returned_path = path(root=folder_path, path_name=file_name)
    assert test_path == returned_path