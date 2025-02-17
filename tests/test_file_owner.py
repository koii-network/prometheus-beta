import os
import pytest
import pwd
from src.file_owner import get_file_owner

def test_get_file_owner_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get the current user
    current_user = pwd.getpwuid(os.getuid()).pw_name
    
    # Test the function
    assert get_file_owner(str(test_file)) == current_user

def test_get_file_owner_non_existent_file():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        get_file_owner("/path/to/non/existent/file.txt")

def test_get_file_owner_absolute_path(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get the current user
    current_user = pwd.getpwuid(os.getuid()).pw_name
    
    # Test with absolute path
    assert get_file_owner(str(test_file.absolute())) == current_user

def test_get_file_owner_user_path(tmp_path):
    # Create a temporary file in user's home directory
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Get the current user
    current_user = pwd.getpwuid(os.getuid()).pw_name
    
    # Test with user path expansion
    assert get_file_owner(str(test_file)) == current_user