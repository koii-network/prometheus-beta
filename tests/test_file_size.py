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

def test_get_file_size_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Check file size
    assert get_file_size(str(test_file)) == 0

def test_get_file_size_non_existent_file():
    # Try to get size of non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_size("non_existent_file.txt")

def test_get_file_size_invalid_input():
    # Test invalid input type
    with pytest.raises(TypeError):
        get_file_size(123)  # Integer instead of string
        
def test_get_file_size_directory(tmp_path):
    # Try to get size of a directory
    with pytest.raises(IsADirectoryError):
        get_file_size(str(tmp_path))