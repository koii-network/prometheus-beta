import os
import pytest
from src.line_counter import count_file_lines

def test_count_file_lines():
    # Create a temporary file for testing
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    
    # Test line counting
    assert count_file_lines(test_file_path) == 3
    
    # Clean up the test file
    os.remove(test_file_path)

def test_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_file.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    # Test empty file
    assert count_file_lines(test_file_path) == 0
    
    # Clean up the test file
    os.remove(test_file_path)

def test_non_existent_file():
    # Test non-existent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        count_file_lines('non_existent_file.txt')