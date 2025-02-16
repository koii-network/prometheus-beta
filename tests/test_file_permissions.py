import os
import pytest
import stat
from src.file_permissions import get_file_permissions

def test_existing_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello")
    
    # Set custom permissions
    test_file.chmod(0o764)  # rwxrw-r--
    
    # Get permissions
    permissions = get_file_permissions(str(test_file))
    
    # Assertions
    assert permissions['owner_read'] == True
    assert permissions['owner_write'] == True
    assert permissions['owner_execute'] == True
    assert permissions['group_read'] == True
    assert permissions['group_write'] == True
    assert permissions['group_execute'] == False
    assert permissions['others_read'] == True
    assert permissions['others_write'] == False
    assert permissions['others_execute'] == False
    assert permissions['is_file'] == True

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_permissions("nonexistent_file.txt")

def test_directory(tmp_path):
    permissions = get_file_permissions(str(tmp_path))
    
    assert permissions['is_directory'] == True
    assert permissions['is_file'] == False

def test_symlink(tmp_path):
    # Create a real file
    real_file = tmp_path / "real_file.txt"
    real_file.write_text("Content")
    
    # Create a symlink
    symlink_path = tmp_path / "symlink.txt"
    symlink_path.symlink_to(real_file)
    
    permissions = get_file_permissions(str(symlink_path))
    
    assert permissions['is_symlink'] == True