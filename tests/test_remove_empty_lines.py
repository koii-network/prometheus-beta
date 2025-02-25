import os
import pytest
from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_basic():
    # Create a test file with empty lines
    test_file_path = 'tests/test_files/sample_with_empty_lines.txt'
    os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
    
    with open(test_file_path, 'w') as f:
        f.write("Line 1\n\n\nLine 2\n   \nLine 3\n")
    
    # Call the function
    remove_empty_lines(test_file_path)
    
    # Check the contents
    with open(test_file_path, 'r') as f:
        lines = f.readlines()
    
    assert lines == ["Line 1\n", "Line 2\n", "Line 3\n"]

def test_remove_empty_lines_completely_empty():
    # Create a completely empty file
    test_file_path = 'tests/test_files/completely_empty.txt'
    
    with open(test_file_path, 'w') as f:
        f.write("\n\n   \n")
    
    # Call the function
    remove_empty_lines(test_file_path)
    
    # Check the contents
    with open(test_file_path, 'r') as f:
        lines = f.readlines()
    
    assert len(lines) == 0

def test_remove_empty_lines_no_empty_lines():
    # Create a file with no empty lines
    test_file_path = 'tests/test_files/no_empty_lines.txt'
    
    with open(test_file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")
    
    # Call the function
    remove_empty_lines(test_file_path)
    
    # Check the contents
    with open(test_file_path, 'r') as f:
        lines = f.readlines()
    
    assert lines == ["Line 1\n", "Line 2\n", "Line 3"]

def test_remove_empty_lines_file_not_found():
    # Test file not found error
    with pytest.raises(FileNotFoundError):
        remove_empty_lines('non_existent_file.txt')

def test_remove_empty_lines_return_value():
    # Create a test file
    test_file_path = 'tests/test_files/return_value.txt'
    os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
    
    with open(test_file_path, 'w') as f:
        f.write("Line 1\n\nLine 2\n")
    
    # Call the function and check return value
    result_path = remove_empty_lines(test_file_path)
    
    assert result_path == test_file_path