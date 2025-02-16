import os
import pytest
from src.file_reader import read_file_contents

def test_read_file_contents_success(tmp_path):
    # Create a temporary test file
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!\nThis is a test file."
    test_file.write_text(test_content)
    
    # Read the file
    result = read_file_contents(str(test_file))
    assert result == test_content

def test_read_file_contents_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    result = read_file_contents(str(test_file))
    assert result == ""

def test_read_file_contents_nonexistent_file():
    # Try to read a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        read_file_contents("/path/to/nonexistent/file.txt")

def test_read_file_contents_long_text(tmp_path):
    # Create a file with longer text
    test_file = tmp_path / "long_text.txt"
    long_text = "This is a longer text\n" * 100
    test_file.write_text(long_text)
    
    # Read the long text file
    result = read_file_contents(str(test_file))
    assert result == long_text