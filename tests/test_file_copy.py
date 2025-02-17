import os
import pytest
import shutil
from src.file_copy import copy_file

@pytest.fixture
def temp_source_file(tmp_path):
    source_file = tmp_path / "source.txt"
    source_file.write_text("Test content")
    return str(source_file)

def test_copy_file_successful(temp_source_file, tmp_path):
    destination_file = str(tmp_path / "destination.txt")
    copy_file(temp_source_file, destination_file)
    
    assert os.path.exists(destination_file)
    assert open(temp_source_file, 'r').read() == open(destination_file, 'r').read()

def test_copy_file_to_nested_directory(temp_source_file, tmp_path):
    nested_dir = tmp_path / "nested"
    destination_file = str(nested_dir / "destination.txt")
    copy_file(temp_source_file, destination_file)
    
    assert os.path.exists(destination_file)

def test_copy_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        copy_file("/path/to/nonexistent/file.txt", "destination.txt")

def test_copy_directory_as_source(tmp_path):
    source_dir = tmp_path / "source_dir"
    source_dir.mkdir()
    
    with pytest.raises(IsADirectoryError):
        copy_file(str(source_dir), "destination.txt")