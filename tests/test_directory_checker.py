import os
import pytest
import tempfile
import shutil

from src.directory_checker import check_directory_exists


def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_directory_exists(temp_dir) is True


def test_nonexistent_directory():
    """Test that a nonexistent directory returns False."""
    # Use a path that is extremely unlikely to exist
    non_existent_path = "/tmp/this_directory_should_not_exist_12345"
    assert check_directory_exists(non_existent_path) is False


def test_file_returns_false():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert check_directory_exists(temp_file.name) is False


def test_tilde_expansion():
    """Test that the function works with ~ (home directory) expansion."""
    home_dir = os.path.expanduser("~")
    assert check_directory_exists("~") is True


def test_none_input_raises_error():
    """Test that None input raises a TypeError."""
    with pytest.raises(TypeError, match="Path cannot be None"):
        check_directory_exists(None)


def test_relative_path():
    """Test checking a relative path."""
    current_dir = os.getcwd()
    try:
        # Try to create a temporary directory
        test_dir = os.path.join(current_dir, "test_temp_dir")
        os.makedirs(test_dir)
        
        # Check relative path
        assert check_directory_exists("test_temp_dir") is True
    finally:
        # Clean up the test directory
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)