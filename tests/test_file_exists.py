import os
import pytest
from src.file_exists import check_file_exists

def test_check_file_exists_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Check that the file exists
    assert check_file_exists(str(test_file)) == True

def test_check_file_exists_non_existing_file(tmp_path):
    # Check a file that does not exist
    non_existing_file = tmp_path / "non_existing_file.txt"
    
    assert check_file_exists(str(non_existing_file)) == False

def test_check_file_exists_directory(tmp_path):
    # Check that the function returns False for a directory
    test_dir = tmp_path / "test_directory"
    test_dir.mkdir()
    
    assert check_file_exists(str(test_dir)) == False

def test_check_file_exists_empty_path():
    # Check behavior with an empty path
    assert check_file_exists("") == False

def test_check_file_exists_invalid_path():
    # Check behavior with an invalid path
    assert check_file_exists("/path/that/definitely/does/not/exist") == False