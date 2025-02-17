import os
import pytest
from src.file_utils import file_exists

def test_file_exists_with_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Check that the file exists
    assert file_exists(str(test_file)) == True

def test_file_exists_with_non_existing_file(tmp_path):
    # Check a file that does not exist
    non_existent_file = tmp_path / "non_existent.txt"
    
    assert file_exists(str(non_existent_file)) == False

def test_file_exists_with_directory(tmp_path):
    # Check that a directory returns False
    test_dir = tmp_path / "test_directory"
    test_dir.mkdir()
    
    assert file_exists(str(test_dir)) == False

def test_file_exists_with_empty_path():
    # Check behavior with an empty path
    assert file_exists("") == False

def test_file_exists_with_relative_path(tmp_path):
    # Create a file and check using a relative path
    current_dir = os.getcwd()
    os.chdir(tmp_path)
    
    test_file = "test_relative.txt"
    with open(test_file, 'w') as f:
        f.write("Relative test")
    
    assert file_exists(test_file) == True
    
    # Clean up and return to original directory
    os.chdir(current_dir)