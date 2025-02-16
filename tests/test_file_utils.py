import os
import pytest
import tempfile
import stat

from src.file_utils import is_file_read_only

def test_is_file_read_only_regular_file():
    """Test regular writable file returns False."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            assert is_file_read_only(temp_file_path) == False
        finally:
            os.unlink(temp_file_path)

def test_is_file_read_only_true_case():
    """Test a read-only file returns True."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            # Make the file read-only
            os.chmod(temp_file_path, stat.S_IRUSR)
            
            assert is_file_read_only(temp_file_path) == True
        finally:
            os.unlink(temp_file_path)

def test_is_file_read_only_nonexistent_file():
    """Test that FileNotFoundError is raised for nonexistent files."""
    with pytest.raises(FileNotFoundError):
        is_file_read_only('nonexistent_file.txt')

def test_is_file_read_only_with_root_user_permissions():
    """Test read-only status for system files that might be accessible by root."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            # Making file readable only by root
            os.chmod(temp_file_path, 0o400)
            
            # Check read-only status
            assert is_file_read_only(temp_file_path) == True
        finally:
            os.unlink(temp_file_path)