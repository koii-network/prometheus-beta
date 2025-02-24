import os
import pytest
from src.file_size import get_file_size

def test_get_file_size_normal():
    # Using README.md as an existing file
    file_path = 'README.md'
    file_size = get_file_size(file_path)
    assert isinstance(file_size, int)
    assert file_size >= 0

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_file_size('non_existent_file.txt')

def test_directory_path():
    with pytest.raises(IsADirectoryError):
        get_file_size('.')

def test_empty_file():
    # Create an empty file for testing
    empty_file_path = 'tests/empty_test_file.txt'
    
    # Ensure the file is created
    with open(empty_file_path, 'w') as f:
        pass
    
    try:
        file_size = get_file_size(empty_file_path)
        assert file_size == 0
    finally:
        # Clean up the temporary file
        os.remove(empty_file_path)