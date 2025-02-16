import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!\nThis is a test file."
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    assert read_file_contents(str(test_file)) == test_content

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    assert read_file_contents(str(test_file)) == ""

def test_nonexistent_file():
    # Attempt to read a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        read_file_contents("nonexistent_file.txt")

def test_read_large_file(tmp_path):
    # Create a large file with multiple lines
    test_file = tmp_path / "large_file.txt"
    large_content = "\n".join([f"Line {i}" for i in range(1000)])
    test_file.write_text(large_content)
    
    # Read and verify the large file
    assert read_file_contents(str(test_file)) == large_content