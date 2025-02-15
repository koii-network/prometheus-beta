import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!\nThis is a test file."
    test_file.write_text(test_content)
    
    # Read the file and check its contents
    result = read_file_contents(str(test_file))
    assert result == test_content

def test_read_non_existing_file():
    # Test reading a non-existing file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existing_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    result = read_file_contents(str(test_file))
    assert result == ""

def test_read_large_file(tmp_path):
    # Create a large file
    test_file = tmp_path / "large_file.txt"
    large_content = "Test content\n" * 10000
    test_file.write_text(large_content)
    
    # Read the large file
    result = read_file_contents(str(test_file))
    assert result == large_content