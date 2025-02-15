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

def test_file_not_found():
    # Test FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.txt was not found."):
        read_file_contents("non_existent_file.txt")

# Note: Testing PermissionError reliably is challenging in a generic test environment
# The actual implementation handles it gracefully if such a scenario occurs