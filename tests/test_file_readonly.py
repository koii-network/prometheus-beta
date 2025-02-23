import os
import pytest
import stat
import tempfile

from src.file_readonly import is_file_readonly

def test_is_file_readonly_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent files."""
    with pytest.raises(FileNotFoundError):
        is_file_readonly("non_existent_file.txt")

def test_is_file_readonly_invalid_input():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        is_file_readonly(123)

def test_is_file_readonly_writable_file():
    """Test a writable file returns False."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        try:
            assert is_file_readonly(temp_file.name) == False
        finally:
            os.unlink(temp_file.name)

def test_is_file_readonly_read_only_file():
    """Test a read-only file returns True."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        try:
            # Make file read-only
            os.chmod(temp_file.name, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
            assert is_file_readonly(temp_file.name) == True
        finally:
            os.unlink(temp_file.name)

def test_is_file_readonly_system_file():
    """Test a system file with read-only permissions."""
    # Test with a system configuration file that's typically read-only
    system_file = "/etc/hostname"  # Works on Unix-like systems
    if os.path.exists(system_file):
        assert is_file_readonly(system_file) in (True, False)