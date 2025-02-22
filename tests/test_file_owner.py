import os
import pwd
import pytest
import tempfile
from src.file_owner import get_file_owner

def test_get_file_owner():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Get current user
        current_user = pwd.getpwuid(os.getuid()).pw_name
        
        # Test that the current user owns the temp file
        owner = get_file_owner(temp_file_path)
        assert owner == current_user
    
    finally:
        # Clean up temporary file
        os.unlink(temp_file_path)

def test_get_file_owner_nonexistent_file():
    # Test for FileNotFoundError
    with pytest.raises(FileNotFoundError):
        get_file_owner('/path/to/nonexistent/file')

def test_get_file_owner_existing_repo_files():
    # Test with existing repository files
    repo_files = [
        '.gitignore',
        'README.md',
        'requirements.txt'
    ]
    
    for file in repo_files:
        # Verify that the function works with existing files
        owner = get_file_owner(file)
        assert isinstance(owner, str)
        assert len(owner) > 0  # Username should have some length