import os
import pytest
from src.file_permissions import change_file_permissions

def test_change_file_permissions_valid():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    # Initial permissions
    initial_mode = os.stat(test_file_path).st_mode

    # Change permissions to read-only
    result = change_file_permissions(test_file_path, 0o444)
    
    # Check if permissions changed
    new_mode = os.stat(test_file_path).st_mode
    assert result is True
    assert new_mode & 0o777 == 0o444
    
    # Clean up
    os.unlink(test_file_path)

def test_change_file_permissions_non_existent_file():
    with pytest.raises(FileNotFoundError):
        change_file_permissions('non_existent_file.txt', 0o755)

def test_change_file_permissions_invalid_mode_too_high():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    with pytest.raises(ValueError):
        change_file_permissions(test_file_path, 0o1000)
    
    # Clean up
    os.unlink(test_file_path)

def test_change_file_permissions_invalid_mode_type():
    # Create a temporary file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    with pytest.raises(TypeError):
        change_file_permissions(test_file_path, '755')
    
    # Clean up
    os.unlink(test_file_path)

def test_change_file_permissions_invalid_file_path():
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o755)