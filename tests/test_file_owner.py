import os
import pytest
import pwd
import getpass

from src.file_owner import get_file_owner

def test_get_file_owner_current_user():
    """Test getting owner of a file created by the current user."""
    # Create a temporary file
    temp_file_path = 'tests/temp_file.txt'
    with open(temp_file_path, 'w') as f:
        f.write('Test file')
    
    try:
        # Get current user
        current_user = getpass.getuser()
        
        # Test the function
        file_owner = get_file_owner(temp_file_path)
        assert file_owner == current_user, f"Expected owner {current_user}, got {file_owner}"
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

def test_get_file_owner_raises_file_not_found():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_owner('non_existent_file.txt')

def test_get_file_owner_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        get_file_owner(123)  # Non-string input

def test_get_file_owner_specific_user():
    """Test getting owner of a file with a specific user."""
    # Create a temporary file
    temp_file_path = 'tests/temp_file_specific.txt'
    with open(temp_file_path, 'w') as f:
        f.write('Test file for specific user')
    
    try:
        # Get file owner using os.stat
        file_stat = os.stat(temp_file_path)
        expected_owner = pwd.getpwuid(file_stat.st_uid).pw_name
        
        # Test the function
        file_owner = get_file_owner(temp_file_path)
        assert file_owner == expected_owner, f"Expected owner {expected_owner}, got {file_owner}"
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)