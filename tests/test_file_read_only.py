import os
import pytest
import tempfile
import stat
import sys
sys.path.append('src')

from file_read_only import is_file_read_only

def test_file_not_read_only():
    """Test that a regular writable file returns False."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert is_file_read_only(temp_file_path) is False
    finally:
        os.unlink(temp_file_path)

def test_file_read_only():
    """Test that a read-only file returns True."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Change file to read-only
        os.chmod(temp_file_path, stat.S_IRUSR)
        
        assert is_file_read_only(temp_file_path) is True
    finally:
        os.unlink(temp_file_path)

def test_nonexistent_file():
    """Test that a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        is_file_read_only('/path/to/nonexistent/file.txt')

def test_invalid_input_type():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_file_read_only(123)
    with pytest.raises(TypeError):
        is_file_read_only(None)