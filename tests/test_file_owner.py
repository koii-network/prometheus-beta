import os
import pytest
import sys
import pwd

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from file_owner import get_file_owner

def test_get_file_owner_existing_file():
    # Use a file that definitely exists
    test_file_path = '/app/repos/repo_12/README.md'
    
    try:
        owner = get_file_owner(test_file_path)
        assert isinstance(owner, str)
        assert len(owner) > 0
    except Exception as e:
        pytest.fail(f"Unexpected error retrieving file owner: {e}")

def test_get_file_owner_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_owner('/nonexistent/path/to/file.txt')

def test_get_file_owner_owner_matches_system():
    test_file_path = '/app/repos/repo_12/README.md'
    
    try:
        file_stat = os.stat(test_file_path)
        system_owner = pwd.getpwuid(file_stat.st_uid).pw_name
        
        file_owner = get_file_owner(test_file_path)
        
        assert file_owner == system_owner
    except Exception as e:
        pytest.fail(f"Error comparing file owner: {e}")