import os
import pytest
import tempfile
from src.delete_empty_lines import delete_empty_lines

def test_delete_empty_lines_in_file():
    # Create a temporary file with empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_input:
        temp_input.write("Hello\n\n\nWorld\n   \nPython\n")
        temp_input_path = temp_input.name
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_output:
        temp_output_path = temp_output.name
    
    # Call the function
    delete_empty_lines(temp_input_path, temp_output_path)
    
    # Check the output file
    with open(temp_output_path, 'r') as f:
        lines = f.readlines()
    
    # Clean up temporary files
    os.unlink(temp_input_path)
    os.unlink(temp_output_path)
    
    # Assert expected results
    assert lines == ["Hello\n", "World\n", "Python\n"]

def test_delete_empty_lines_in_place():
    # Create a temporary file with empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\n\n\nWorld\n   \nPython\n")
        temp_file_path = temp_file.name
    
    # Call the function
    delete_empty_lines(temp_file_path)
    
    # Check the file
    with open(temp_file_path, 'r') as f:
        lines = f.readlines()
    
    # Clean up temporary file
    os.unlink(temp_file_path)
    
    # Assert expected results
    assert lines == ["Hello\n", "World\n", "Python\n"]

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        delete_empty_lines("non_existent_file.txt")

def test_empty_file():
    # Create a temporary empty file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_input:
        temp_input_path = temp_input.name
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_output:
        temp_output_path = temp_output.name
    
    # Call the function
    delete_empty_lines(temp_input_path, temp_output_path)
    
    # Check the output file
    with open(temp_output_path, 'r') as f:
        lines = f.readlines()
    
    # Clean up temporary files
    os.unlink(temp_input_path)
    os.unlink(temp_output_path)
    
    # Assert expected results
    assert lines == []