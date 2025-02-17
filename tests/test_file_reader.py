import os
import pytest
from src.file_reader import read_file_contents

def test_read_valid_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!"
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    assert read_file_contents(str(test_file)) == test_content

def test_read_nonexistent_file():
    # Test reading a nonexistent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_file_contents("nonexistent_file.txt")

def test_read_directory(tmp_path):
    # Test attempting to read a directory raises IsADirectoryError
    with pytest.raises(IsADirectoryError):
        read_file_contents(str(tmp_path))

def test_read_empty_file(tmp_path):
    # Create an empty file and verify it returns an empty string
    empty_file = tmp_path / "empty_file.txt"
    empty_file.touch()
    
    assert read_file_contents(str(empty_file)) == ""