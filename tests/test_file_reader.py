import os
import pytest
from src.file_reader import read_text_file

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!\nThis is a test file."
    test_file.write_text(test_content)
    
    # Read the file
    result = read_text_file(str(test_file))
    assert result == test_content

def test_read_nonexistent_file():
    # Test reading a non-existent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_text_file("non_existent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty file and test reading it
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    result = read_text_file(str(test_file))
    assert result == ""

def test_read_file_with_special_characters(tmp_path):
    # Test reading a file with special characters and unicode
    test_file = tmp_path / "special_chars.txt"
    test_content = "Hello! こんにちは\nSpecial chars: !@#$%^&*()"
    test_file.write_text(test_content)
    
    result = read_text_file(str(test_file))
    assert result == test_content