import os
import pytest
import tempfile
from src.file_permissions import get_file_permissions

def test_get_file_permissions():
    # Create a temporary file with specific permissions
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name
        
        # Set file permissions: 755 (rwxr-xr-x)
        os.chmod(file_path, 0o755)
        
        # Get file permissions
        permissions = get_file_permissions(file_path)
        
        # Verify permissions
        assert permissions == {
            'owner_read': True,
            'owner_write': True,
            'owner_execute': True,
            'group_read': True,
            'group_write': False,
            'group_execute': True,
            'others_read': True,
            'others_write': False,
            'others_execute': True,
            'octal_permissions': '755'
        }
        
        # Clean up
        os.unlink(file_path)

def test_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_permissions('nonexistent_file.txt')

def test_no_read_permissions(mocker):
    # Mock os.stat to simulate permission error
    mocker.patch('os.stat', side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        get_file_permissions('/path/to/restricted/file')