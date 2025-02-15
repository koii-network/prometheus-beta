import os
import pytest
from src.file_size import get_file_size

def test_get_file_size_existing_file(tmp_path):
    # Create a test file with known content
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, World!")
    
    # Get the file size
    file_size = get_file_size(str(test_file))
    
    # Assert the file size matches expected length
    assert file_size == len("Hello, World!")

def test_get_file_size_nonexistent_file():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_size("non_existent_file.txt")

def test_get_file_size_directory(tmp_path):
    # Test that IsADirectoryError is raised when path is a directory
    with pytest.raises(IsADirectoryError):
        get_file_size(str(tmp_path))

def test_get_file_size_zero_byte_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Get the file size
    file_size = get_file_size(str(test_file))
    
    # Assert file size is 0
    assert file_size == 0

def test_get_file_size_existing_repo_file():
    # Test getting size of an existing repository file
    readme_path = "README.md"
    file_size = get_file_size(readme_path)
    
    # Assert that the file exists and has a non-negative size
    assert file_size >= 0