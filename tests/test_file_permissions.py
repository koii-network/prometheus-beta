import os
import pytest
import stat
from src.file_permissions import change_file_permissions

def test_change_file_permissions_valid():
    # Create a temporary test file
    test_file = 'tests/test_file.txt'
    with open(test_file, 'w') as f:
        f.write('Test content')
    
    # Initial mode check
    initial_mode = os.stat(test_file).st_mode
    
    # Change permissions to read-only for all
    result = change_file_permissions(test_file, 0o444)
    
    # Verify permissions changed
    new_mode = os.stat(test_file).st_mode
    assert result == True
    assert stat.S_IMODE(new_mode) == 0o444
    
    # Clean up
    os.unlink(test_file)

def test_change_file_permissions_file_not_found():
    with pytest.raises(FileNotFoundError):
        change_file_permissions('non_existent_file.txt', 0o755)

def test_change_file_permissions_invalid_path_type():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o755)

def test_change_file_permissions_invalid_mode_type():
    with pytest.raises(TypeError):
        change_file_permissions('some_file.txt', '755')

def test_change_file_permissions_executable():
    # Create a temporary test file
    test_file = 'tests/test_executable.sh'
    with open(test_file, 'w') as f:
        f.write('#!/bin/bash\necho "Hello"')
    
    # Change to executable
    result = change_file_permissions(test_file, 0o755)
    
    # Verify permissions
    new_mode = os.stat(test_file).st_mode
    assert result == True
    assert stat.S_IMODE(new_mode) == 0o755
    
    # Clean up
    os.unlink(test_file)