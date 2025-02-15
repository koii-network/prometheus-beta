import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known contents
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, this is a test file!"
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    assert read_file_contents(str(test_file)) == test_content

def test_read_nonexistent_file():
    # Verify FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_contents("nonexistent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty file and verify empty string is returned
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    assert read_file_contents(str(test_file)) == ""

def test_read_directory(tmp_path):
    # Verify IsADirectoryError is raised when trying to read a directory
    with pytest.raises(IsADirectoryError):
        read_file_contents(str(tmp_path))