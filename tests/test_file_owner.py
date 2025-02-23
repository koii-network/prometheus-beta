import os
import pytest
import pwd
import tempfile
from src.file_owner import get_file_owner

def test_get_file_owner_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Get the current user
        current_user = pwd.getpwuid(os.getuid()).pw_name
        
        # Test the function
        owner = get_file_owner(temp_path)
        assert owner == current_user, f"Expected {current_user}, got {owner}"
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_get_file_owner_non_existent_file():
    with pytest.raises(FileNotFoundError):
        get_file_owner("/path/to/non/existent/file.txt")

def test_get_file_owner_invalid_input():
    with pytest.raises(TypeError):
        get_file_owner(123)  # Non-string input

def test_get_file_owner_user_path_expansion():
    # Test path expansion (using home directory)
    home_file_path = os.path.join("~", "testfile.txt")
    
    # Create a temporary file in home directory
    expanded_path = os.path.expanduser(home_file_path)
    with open(expanded_path, 'w') as f:
        f.write("test")
    
    try:
        current_user = pwd.getpwuid(os.getuid()).pw_name
        owner = get_file_owner(home_file_path)
        assert owner == current_user
    
    finally:
        # Clean up
        os.unlink(expanded_path)