import os
import pytest
import tempfile
import shutil
from src.directory_utils import check_directory_exists

def test_check_directory_exists_valid_directory():
    """Test checking an existing directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_directory_exists(temp_dir) is True

def test_check_directory_exists_non_existent_directory():
    """Test checking a non-existent directory."""
    non_existent_path = "/path/to/non/existent/directory"
    assert check_directory_exists(non_existent_path) is False

def test_check_directory_exists_file_path():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert check_directory_exists(temp_file.name) is False

def test_check_directory_exists_home_directory():
    """Test checking home directory."""
    home_dir = os.path.expanduser("~")
    assert check_directory_exists(home_dir) is True

def test_check_directory_exists_invalid_path_type():
    """Test that an invalid path type raises a TypeError."""
    with pytest.raises(TypeError, match="Path must be a string or path-like object"):
        check_directory_exists(123)

def test_check_directory_exists_relative_path():
    """Test checking a relative path."""
    current_dir = "."
    assert check_directory_exists(current_dir) is True

def test_check_directory_exists_path_with_unicode():
    """Test checking a directory path with Unicode characters."""
    with tempfile.TemporaryDirectory(prefix="тест_") as temp_dir:
        assert check_directory_exists(temp_dir) is True