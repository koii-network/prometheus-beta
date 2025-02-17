import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!"
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    assert read_file_contents(str(test_file)) == test_content

def test_read_file_not_found():
    # Attempt to read a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty file and test reading it
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    assert read_file_contents(str(test_file)) == ""

def test_read_file_with_special_characters(tmp_path):
    # Test reading a file with special characters
    test_file = tmp_path / "special_chars.txt"
    test_content = "Line 1\nLine 2 with special chars: !@#$%^&*()"
    test_file.write_text(test_content)
    
    assert read_file_contents(str(test_file)) == test_content