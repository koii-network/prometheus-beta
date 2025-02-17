import os
import pytest
import stat
from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Set specific permissions
    test_file.chmod(0o764)  # rwxrw-r--
    
    # Get file permissions
    permissions = get_file_permissions(str(test_file))
    
    # Verify permissions
    assert permissions['owner_read'] == True
    assert permissions['owner_write'] == True
    assert permissions['owner_execute'] == True
    assert permissions['group_read'] == True
    assert permissions['group_write'] == True
    assert permissions['group_execute'] == False
    assert permissions['others_read'] == True
    assert permissions['others_write'] == False
    assert permissions['others_execute'] == False
    assert permissions['octal_permissions'] == '764'

def test_get_file_permissions_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_permissions('nonexistent_file.txt')

def test_get_file_permissions_multiple_files(tmp_path):
    # Create multiple test files with different permissions
    file1 = tmp_path / "file1.txt"
    file1.write_text("File 1")
    file1.chmod(0o644)  # rw-r--r--
    
    file2 = tmp_path / "file2.txt"
    file2.write_text("File 2")
    file2.chmod(0o755)  # rwxr-xr-x
    
    # Test both files
    perm1 = get_file_permissions(str(file1))
    perm2 = get_file_permissions(str(file2))
    
    assert perm1['octal_permissions'] == '644'
    assert perm2['octal_permissions'] == '755'