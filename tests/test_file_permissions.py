import os
import pytest
import stat
import tempfile

from src.file_permissions import change_file_permissions

def test_change_file_permissions_valid():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Initially, the file will have default permissions
        original_mode = os.stat(temp_path).st_mode
        
        # Change permissions to read-only for owner
        change_file_permissions(temp_path, 0o400)
        
        # Get new mode
        new_mode = os.stat(temp_path).st_mode
        
        # Check if permissions were changed correctly
        assert stat.S_IMODE(new_mode) == 0o400
        assert new_mode != original_mode
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_change_file_permissions_invalid_path():
    # Test with non-existent file
    with pytest.raises(FileNotFoundError):
        change_file_permissions('/path/to/nonexistent/file', 0o755)

def test_change_file_permissions_invalid_mode_type():
    # Test with invalid mode type
    with pytest.raises(TypeError):
        change_file_permissions('/some/file', '755')

def test_change_file_permissions_invalid_path_type():
    # Test with invalid path type
    with pytest.raises(TypeError):
        change_file_permissions(123, 0o755)

def test_multiple_permission_changes():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # Change permissions multiple times
        change_file_permissions(temp_path, 0o400)  # Read-only
        mode1 = os.stat(temp_path).st_mode
        
        change_file_permissions(temp_path, 0o755)  # Full permissions
        mode2 = os.stat(temp_path).st_mode
        
        # Check each mode change
        assert stat.S_IMODE(mode1) == 0o400
        assert stat.S_IMODE(mode2) == 0o755
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)