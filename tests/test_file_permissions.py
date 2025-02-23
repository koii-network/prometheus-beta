import os
import pytest
import tempfile
import stat
from src.file_permissions import get_file_permissions

def create_test_file(mode=0o644):
    """Create a temporary file with specified permissions."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        os.chmod(temp_file.name, mode)
        return temp_file.name

def test_get_file_permissions_standard():
    """Test getting permissions for a standard file."""
    test_file = create_test_file(0o644)
    try:
        permissions = get_file_permissions(test_file)
        
        assert 'mode' in permissions
        assert 'readable' in permissions
        assert 'writable' in permissions
        assert 'executable' in permissions
        assert 'permission_string' in permissions
        
        assert permissions['readable'] is True
        assert permissions['writable'] is True
        assert permissions['executable'] is False
        assert permissions['permission_string'] == 'rw-r--r--'
    finally:
        os.unlink(test_file)

def test_get_file_permissions_executable():
    """Test getting permissions for an executable file."""
    test_file = create_test_file(0o755)
    try:
        permissions = get_file_permissions(test_file)
        
        assert permissions['readable'] is True
        assert permissions['writable'] is True
        assert permissions['executable'] is True
        assert permissions['permission_string'] == 'rwxr-xr-x'
    finally:
        os.unlink(test_file)

def test_get_file_permissions_nonexistent_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_permissions('/path/to/nonexistent/file')

def test_get_file_permissions_no_read_permission(monkeypatch):
    """Test handling of files with no read permission."""
    def mock_access(path, mode):
        return False
    
    monkeypatch.setattr(os, 'access', mock_access)
    
    test_file = create_test_file()
    try:
        permissions = get_file_permissions(test_file)
        
        assert permissions['readable'] is False
        assert permissions['writable'] is False
        assert permissions['executable'] is False
    finally:
        os.unlink(test_file)