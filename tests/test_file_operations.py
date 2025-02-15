import os
import pytest
from src.file_operations import delete_file

def test_delete_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_delete.txt"
    test_file.write_text("Test content")
    
    # Verify file exists before deletion
    assert test_file.exists()
    
    # Delete the file
    delete_file(str(test_file))
    
    # Verify file no longer exists
    assert not test_file.exists()

def test_delete_non_existent_file():
    # Attempt to delete a non-existent file should raise FileNotFoundError
    with pytest.raises(FileNotFoundError):
        delete_file("non_existent_file.txt")

def test_delete_directory(tmp_path):
    # Attempt to delete a directory should raise IsADirectoryError
    with pytest.raises(IsADirectoryError):
        delete_file(str(tmp_path))

def test_delete_invalid_input():
    # Attempt to delete with non-string input should raise TypeError
    with pytest.raises(TypeError):
        delete_file(123)  # Integer instead of string