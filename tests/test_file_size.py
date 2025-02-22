import os
import pytest
from src.file_size import get_file_size

def test_get_file_size_existing_file(tmp_path):
    # Create a test file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!"
    test_file.write_text(test_content)
    
    # Check file size
    assert get_file_size(str(test_file)) == len(test_content)

def test_get_file_size_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_size("nonexistent_file.txt")

def test_get_file_size_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Check empty file size
    assert get_file_size(str(test_file)) == 0

def test_get_file_size_with_directory(tmp_path):
    with pytest.raises(IsADirectoryError):
        get_file_size(str(tmp_path))