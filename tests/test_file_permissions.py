import os
import pytest
import stat
from src.file_permissions import get_file_permissions

def test_get_file_permissions(tmp_path):
    # Create a test file with specific permissions
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Set specific permissions (rw-r--r--)
    test_file.chmod(0o644)
    
    # Get permissions
    perms = get_file_permissions(str(test_file))
    
    # Verify permissions
    assert perms['octal'] == '0o644'
    assert perms['readable'] == 'rw-r--r--'
    
    # Owner permissions
    assert perms['owner_read'] == True
    assert perms['owner_write'] == True
    assert perms['owner_execute'] == False
    
    # Group permissions
    assert perms['group_read'] == True
    assert perms['group_write'] == False
    assert perms['group_execute'] == False
    
    # Others permissions
    assert perms['others_read'] == True
    assert perms['others_write'] == False
    assert perms['others_execute'] == False

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        get_file_permissions('/path/to/nonexistent/file.txt')

def test_different_file_permissions(tmp_path):
    # Test executable file (rwxr-xr-x)
    test_file = tmp_path / "executable_file"
    test_file.write_text("#!/bin/bash\necho 'test'")
    test_file.chmod(0o755)
    
    perms = get_file_permissions(str(test_file))
    
    assert perms['octal'] == '0o755'
    assert perms['readable'] == 'rwxr-xr-x'
    assert perms['owner_execute'] == True
    assert perms['group_execute'] == True
    assert perms['others_execute'] == True