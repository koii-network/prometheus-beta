import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")
    
    # Read the file and verify contents
    content = read_file_contents(str(test_file))
    assert content == "Hello, World!"

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    
    # Read the empty file
    content = read_file_contents(str(test_file))
    assert content == ""

def test_file_not_found():
    # Attempt to read a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existent_file.txt")

def test_file_with_special_characters(tmp_path):
    # Create a file with special characters
    test_file = tmp_path / "special_chars.txt"
    test_content = "Line 1\nLine 2 with SpecialChars: !@#$%^&*()"
    test_file.write_text(test_content)
    
    # Read and verify the content
    content = read_file_contents(str(test_file))
    assert content == test_content