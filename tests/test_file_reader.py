import os
import pytest
from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line():
    # Create a temporary test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello\nWorld\nPython\n")
    
    # Test reading the file
    lines = read_file_line_by_line(test_file_path)
    
    # Assertions
    assert lines == ["Hello\n", "World\n", "Python\n"]
    assert len(lines) == 3
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_line_by_line_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_file.txt'
    open(test_file_path, 'w').close()
    
    # Test reading an empty file
    lines = read_file_line_by_line(test_file_path)
    
    # Assertions
    assert lines == []
    
    # Clean up the test file
    os.remove(test_file_path)

def test_read_file_not_found():
    # Test reading a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line('non_existent_file.txt')