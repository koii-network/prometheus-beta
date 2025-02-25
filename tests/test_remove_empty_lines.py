import os
import pytest
from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_in_place():
    # Create a test file with empty lines
    test_file_path = 'tests/test_empty_lines.txt'
    with open(test_file_path, 'w') as f:
        f.write("Line 1\n\n\nLine 2\n   \nLine 3\n")
    
    # Remove empty lines
    remove_empty_lines(test_file_path)
    
    # Check content
    with open(test_file_path, 'r') as f:
        lines = f.readlines()
    
    assert lines == ["Line 1\n", "Line 2\n", "Line 3\n"]
    
    # Clean up test file
    os.remove(test_file_path)

def test_remove_empty_lines_to_new_file():
    # Create a test file with empty lines
    test_input_path = 'tests/test_input.txt'
    test_output_path = 'tests/test_output.txt'
    
    with open(test_input_path, 'w') as f:
        f.write("Line 1\n\n\nLine 2\n   \nLine 3\n")
    
    # Remove empty lines to a new file
    remove_empty_lines(test_input_path, test_output_path)
    
    # Check content of output file
    with open(test_output_path, 'r') as f:
        lines = f.readlines()
    
    assert lines == ["Line 1\n", "Line 2\n", "Line 3\n"]
    
    # Clean up test files
    os.remove(test_input_path)
    os.remove(test_output_path)

def test_remove_empty_lines_empty_file():
    # Create an empty file
    test_file_path = 'tests/test_empty_file.txt'
    open(test_file_path, 'w').close()
    
    # Remove empty lines
    remove_empty_lines(test_file_path)
    
    # Check content
    with open(test_file_path, 'r') as f:
        lines = f.readlines()
    
    assert lines == []
    
    # Clean up test file
    os.remove(test_file_path)

def test_remove_empty_lines_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        remove_empty_lines('non_existent_file.txt')