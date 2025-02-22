import os
import pytest
import shutil
from src.file_rename import rename_file

@pytest.fixture
def temp_test_files(tmp_path):
    # Create a temporary test directory and files
    source_file = tmp_path / "source_file.txt"
    source_file.write_text("Test content")
    return tmp_path, source_file

def test_rename_file_success(temp_test_files):
    temp_dir, source_file = temp_test_files
    destination_path = str(temp_dir / "renamed_file.txt")
    
    result = rename_file(str(source_file), destination_path)
    
    assert result == destination_path
    assert os.path.exists(destination_path)
    assert not os.path.exists(str(source_file))

def test_rename_to_different_directory(temp_test_files):
    temp_dir, source_file = temp_test_files
    new_subdir = temp_dir / "subdir"
    destination_path = str(new_subdir / "renamed_file.txt")
    
    result = rename_file(str(source_file), destination_path)
    
    assert result == destination_path
    assert os.path.exists(destination_path)
    assert not os.path.exists(str(source_file))

def test_rename_file_not_found():
    with pytest.raises(FileNotFoundError):
        rename_file("non_existent_file.txt", "new_file.txt")

def test_rename_source_is_directory(tmp_path):
    with pytest.raises(IsADirectoryError):
        rename_file(str(tmp_path), "some_file.txt")

def test_rename_file_same_name(temp_test_files):
    temp_dir, source_file = temp_test_files
    result = rename_file(str(source_file), str(source_file))
    
    assert result == str(source_file)
    assert os.path.exists(str(source_file))