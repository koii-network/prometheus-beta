import os
import pytest
from src.file_line_counter import count_file_lines

def test_count_file_lines():
    # Create a temporary file with known content
    with open('test_lines.txt', 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    
    # Test counting lines in the file
    assert count_file_lines('test_lines.txt') == 3
    
    # Clean up the test file
    os.remove('test_lines.txt')

def test_count_empty_file():
    # Create an empty file
    with open('empty_file.txt', 'w') as f:
        pass
    
    # Test counting lines in an empty file
    assert count_file_lines('empty_file.txt') == 0
    
    # Clean up the test file
    os.remove('empty_file.txt')

def test_file_not_found():
    # Test that a FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        count_file_lines('non_existent_file.txt')