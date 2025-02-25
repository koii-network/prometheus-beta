import os
import stat
import pytest
from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file(tmp_path):
    # Create a test file with specific permissions
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    test_file.chmod(0o644)  # rw-r--r--
    
    permissions = get_file_permissions(str(test_file))
    
    assert permissions['numeric'] == 0o644
    assert permissions['readable'] == 'rw-r--r--'
    assert permissions['owner_read'] is True
    assert permissions['owner_write'] is True
    assert permissions['owner_execute'] is False
    assert permissions['group_read'] is True
    assert permissions['group_write'] is False
    assert permissions['group_execute'] is False
    assert permissions['others_read'] is True
    assert permissions['others_write'] is False
    assert permissions['others_execute'] is False

def test_get_file_permissions_executable(tmp_path):
    # Create an executable file
    test_file = tmp_path / "test_script.sh"
    test_file.write_text("#!/bin/bash\necho 'Hello'")
    test_file.chmod(0o755)  # rwxr-xr-x
    
    permissions = get_file_permissions(str(test_file))
    
    assert permissions['numeric'] == 0o755
    assert permissions['readable'] == 'rwxr-xr-x'
    assert permissions['owner_execute'] is True
    assert permissions['group_execute'] is True
    assert permissions['others_execute'] is True

def test_get_file_permissions_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_permissions("/path/to/nonexistent/file.txt")

def test_get_file_permissions_no_read_permission(tmp_path):
    # Create a file with no read permissions
    test_file = tmp_path / "no_read_file.txt"
    test_file.write_text("Hidden content")
    test_file.chmod(0o000)  # No permissions
    
    permissions = get_file_permissions(str(test_file))
    
    assert permissions['numeric'] == 0o000
    assert permissions['readable'] == '---------'
    assert all(not permissions[key] for key in [
        'owner_read', 'owner_write', 'owner_execute',
        'group_read', 'group_write', 'group_execute',
        'others_read', 'others_write', 'others_execute'
    ])