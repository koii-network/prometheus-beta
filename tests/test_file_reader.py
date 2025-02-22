import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_success():
    # Create a temporary test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello\nWorld\nPython\n")
    
    # Read the file
    lines = read_file_line_by_line(test_file_path)
    
    # Verify the lines
    assert lines == ["Hello\n", "World\n", "Python\n"]
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_line_by_line_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_file.txt'
    open(test_file_path, 'w').close()
    
    # Read the file
    lines = read_file_line_by_line(test_file_path)
    
    # Verify empty list
    assert lines == []
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_line_by_line_file_not_found():
    # Attempt to read a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line('non_existent_file.txt')