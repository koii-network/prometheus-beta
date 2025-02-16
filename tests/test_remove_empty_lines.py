import os
import pytest
import tempfile
from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_success():
    # Create a temporary file with empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\n\n\nWorld\n\n")
        temp_file_path = temp_file.name
    
    try:
        # Call the function
        result = remove_empty_lines(temp_file_path)
        
        # Check the result and content
        assert result == True
        
        with open(temp_file_path, 'r') as f:
            content = f.read()
        
        assert content == "Hello\nWorld\n"
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_remove_empty_lines_no_changes():
    # Create a temporary file without empty lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\nWorld\n")
        temp_file_path = temp_file.name
    
    try:
        # Call the function
        result = remove_empty_lines(temp_file_path)
        
        # Check the result and content
        assert result == False
        
        with open(temp_file_path, 'r') as f:
            content = f.read()
        
        assert content == "Hello\nWorld\n"
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_remove_empty_lines_whitespace_only():
    # Create a temporary file with whitespace-only lines
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\n   \n\t\n\nWorld\n")
        temp_file_path = temp_file.name
    
    try:
        # Call the function
        result = remove_empty_lines(temp_file_path)
        
        # Check the result and content
        assert result == True
        
        with open(temp_file_path, 'r') as f:
            content = f.read()
        
        assert content == "Hello\nWorld\n"
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_remove_empty_lines_file_not_found():
    with pytest.raises(FileNotFoundError):
        remove_empty_lines("non_existent_file.txt")

def test_remove_empty_lines_empty_file():
    # Create a temporary empty file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Call the function
        result = remove_empty_lines(temp_file_path)
        
        # Check the result and content
        assert result == False
        
        with open(temp_file_path, 'r') as f:
            content = f.read()
        
        assert content == ""
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)