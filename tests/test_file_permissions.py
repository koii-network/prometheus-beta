import os
import pytest
import stat
from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file(tmp_path):
    # Create a test file with specific permissions
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("test content")
    
    # Change file permissions to 644
    test_file.chmod(0o644)
    
    # Get permissions
    perms = get_file_permissions(str(test_file))
    
    # Verify results
    assert perms['numeric'] == '644'
    assert perms['readable'] == 'rw-r--r--'
    assert perms['owner_can_read'] == True
    assert perms['owner_can_write'] == True
    assert perms['owner_can_execute'] == False
    assert perms['group_can_read'] == True
    assert perms['group_can_write'] == False
    assert perms['group_can_execute'] == False
    assert perms['others_can_read'] == True
    assert perms['others_can_write'] == False
    assert perms['others_can_execute'] == False

def test_get_file_permissions_executable(tmp_path):
    # Create a test file with execute permissions
    test_file = tmp_path / "script.sh"
    test_file.write_text("#!/bin/bash\necho 'test'")
    
    # Change file permissions to 755
    test_file.chmod(0o755)
    
    # Get permissions
    perms = get_file_permissions(str(test_file))
    
    # Verify results
    assert perms['numeric'] == '755'
    assert perms['readable'] == 'rwxr-xr-x'
    assert perms['owner_can_execute'] == True
    assert perms['group_can_execute'] == True
    assert perms['others_can_execute'] == True

def test_get_file_permissions_no_permissions(tmp_path):
    # Create a test file with no permissions
    test_file = tmp_path / "secret.txt"
    test_file.write_text("private content")
    
    # Change file permissions to 000
    test_file.chmod(0o000)
    
    # Get permissions
    perms = get_file_permissions(str(test_file))
    
    # Verify results
    assert perms['numeric'] == '000'
    assert perms['readable'] == '---------'
    assert perms['owner_can_read'] == False
    assert perms['owner_can_write'] == False
    assert perms['owner_can_execute'] == False
    assert perms['group_can_read'] == False
    assert perms['group_can_write'] == False
    assert perms['group_can_execute'] == False
    assert perms['others_can_read'] == False
    assert perms['others_can_write'] == False
    assert perms['others_can_execute'] == False

def test_get_file_permissions_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_permissions("/path/to/nonexistent/file.txt")