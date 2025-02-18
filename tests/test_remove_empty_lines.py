import os
import pytest
import tempfile
from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_basic():
    # Create a temporary file with mixed empty and non-empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\n\n\nWorld\n\n   \n\nPython\n")
        temp_file_path = temp_file.name
    
    # Call the function
    remove_empty_lines(temp_file_path)
    
    # Read the file and verify contents
    with open(temp_file_path, 'r') as f:
        lines = f.readlines()
    
    # Clean up the temporary file
    os.unlink(temp_file_path)
    
    # Assert only non-empty lines remain
    assert lines == ["Hello\n", "World\n", "Python\n"]

def test_remove_empty_lines_all_empty():
    # Create a temporary file with only empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("\n\n   \n\n")
        temp_file_path = temp_file.name
    
    # Call the function
    remove_empty_lines(temp_file_path)
    
    # Read the file and verify contents
    with open(temp_file_path, 'r') as f:
        lines = f.readlines()
    
    # Clean up the temporary file
    os.unlink(temp_file_path)
    
    # Assert file is now empty
    assert lines == []

def test_remove_empty_lines_no_empty():
    # Create a temporary file with no empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\nWorld\nPython\n")
        temp_file_path = temp_file.name
    
    # Call the function
    remove_empty_lines(temp_file_path)
    
    # Read the file and verify contents
    with open(temp_file_path, 'r') as f:
        lines = f.readlines()
    
    # Clean up the temporary file
    os.unlink(temp_file_path)
    
    # Assert contents remain unchanged
    assert lines == ["Hello\n", "World\n", "Python\n"]

def test_remove_empty_lines_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        remove_empty_lines("non_existent_file.txt")