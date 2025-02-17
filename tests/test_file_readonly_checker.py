import os
import pytest
import tempfile
import stat

from src.file_readonly_checker import is_file_readonly

def test_readable_writable_file():
    """Test a normal readable and writable file."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            assert is_file_readonly(temp_file_path) is False
        finally:
            os.unlink(temp_file_path)

def test_readonly_file():
    """Test a file made read-only."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            # Change file permissions to read-only
            os.chmod(temp_file_path, stat.S_IRUSR)
            assert is_file_readonly(temp_file_path) is True
        finally:
            # Restore write permissions and delete file
            os.chmod(temp_file_path, stat.S_IRUSR | stat.S_IWUSR)
            os.unlink(temp_file_path)

def test_nonexistent_file():
    """Test behavior when file does not exist."""
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        nonexistent_path = temp_file.name  # File is already deleted
        with pytest.raises(FileNotFoundError):
            is_file_readonly(nonexistent_path)

def test_file_read_permissions():
    """Additional test to verify read-only status."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            # Set read-only permissions
            os.chmod(temp_file_path, stat.S_IRUSR)
            
            # Verify read-only status
            assert is_file_readonly(temp_file_path) is True
        finally:
            # Clean up
            os.chmod(temp_file_path, stat.S_IRUSR | stat.S_IWUSR)
            os.unlink(temp_file_path)