import os
import pytest
import tempfile
import stat
import sys
import pathlib

# Add the src directory to the Python path
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / 'src'))

from file_permissions import is_file_read_only

def test_is_file_read_only_regular_writable_file():
    """Test a regular writable file returns False."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert is_file_read_only(temp_file_path) is False
    finally:
        os.unlink(temp_file_path)

def test_is_file_read_only_read_only_file():
    """Test a read-only file returns True."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Make the file read-only
        os.chmod(temp_file_path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        
        assert is_file_read_only(temp_file_path) is True
    finally:
        os.unlink(temp_file_path)

def test_is_file_read_only_nonexistent_file():
    """Test that a FileNotFoundError is raised for non-existent files."""
    with pytest.raises(FileNotFoundError):
        is_file_read_only('/path/to/nonexistent/file.txt')

def test_is_file_read_only_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        is_file_read_only(123)
    
    with pytest.raises(TypeError):
        is_file_read_only(None)

def test_is_file_read_only_symlink():
    """Test behavior with a read-only symlink."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file_path = temp_file.name
        symlink_path = temp_file_path + '_symlink'
    
    try:
        # Create a symlink and make it read-only
        os.symlink(temp_file_path, symlink_path)
        os.chmod(symlink_path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        
        assert is_file_read_only(symlink_path) is True
    finally:
        os.unlink(temp_file_path)
        os.unlink(symlink_path)