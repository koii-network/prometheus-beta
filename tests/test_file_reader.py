import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!\nThis is a test file."
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    result = read_file_contents(str(test_file))
    assert result == test_content

def test_read_nonexistent_file():
    # Test reading a file that doesn't exist
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.txt was not found."):
        read_file_contents("non_existent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    result = read_file_contents(str(test_file))
    assert result == ""

def test_read_file_with_special_characters(tmp_path):
    # Create a file with special characters
    test_file = tmp_path / "special_chars.txt"
    test_content = "Line with special chars: @#$%^&*()_+"
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    result = read_file_contents(str(test_file))
    assert result == test_content