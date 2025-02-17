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

def test_read_nonexistent_file():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Verify reading an empty file returns an empty string
    assert read_file_contents(str(test_file)) == ""

def test_read_large_file(tmp_path):
    # Create a large file and verify it can be read
    test_file = tmp_path / "large_file.txt"
    large_content = "a" * 1000000  # 1 million characters
    test_file.write_text(large_content)
    
    assert read_file_contents(str(test_file)) == large_content