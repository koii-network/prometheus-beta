import os
import pytest
from src.file_line_counter import count_file_lines

def test_count_file_lines_normal():
    # Create a temporary test file
    test_file_path = 'tests/test_sample.txt'
    with open(test_file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    try:
        # Test counting lines
        assert count_file_lines(test_file_path) == 3
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_count_empty_file():
    # Create an empty file
    test_file_path = 'tests/empty_test_file.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    try:
        # Test empty file
        assert count_file_lines(test_file_path) == 0
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_file_not_found():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        count_file_lines('non_existent_file.txt')

def test_large_file():
    # Create a large file
    test_file_path = 'tests/large_test_file.txt'
    with open(test_file_path, 'w') as f:
        for i in range(10000):
            f.write(f"Line {i}\n")
    
    try:
        # Test large file
        assert count_file_lines(test_file_path) == 10000
    finally:
        # Clean up the test file
        os.remove(test_file_path)