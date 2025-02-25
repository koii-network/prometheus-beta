import os
import pytest
import tempfile
from src.file_owner import get_file_owner

def test_get_file_owner_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Get current user
        current_user = os.getlogin()
        
        # Get file owner
        owner = get_file_owner(temp_path)
        
        # Assert the owner matches current user
        assert owner == current_user
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_get_file_owner_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_owner('/path/to/nonexistent/file')

def test_get_file_owner_invalid_input():
    with pytest.raises(TypeError):
        get_file_owner(123)  # Non-string input

def test_get_file_owner_relative_path():
    # Create a temporary file in current directory
    with tempfile.NamedTemporaryFile(delete=False, dir=os.getcwd()) as temp_file:
        temp_filename = os.path.basename(temp_file.name)
    
    try:
        # Get current user
        current_user = os.getlogin()
        
        # Get file owner using relative path
        owner = get_file_owner(temp_filename)
        
        # Assert the owner matches current user
        assert owner == current_user
    finally:
        # Clean up the temporary file
        os.unlink(temp_filename)