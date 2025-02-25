import os
import pytest
import tempfile

from src.file_exists import check_file_exists


def test_existing_file():
    """Test that an existing file returns True."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert check_file_exists(temp_file_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)


def test_non_existing_file():
    """Test that a non-existing file returns False."""
    non_existing_path = "/path/to/definitely/non/existing/file.txt"
    assert check_file_exists(non_existing_path) is False


def test_directory_returns_false():
    """Test that a directory returns False."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_file_exists(temp_dir) is False


def test_invalid_input_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="File path must be a string"):
        check_file_exists(123)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        check_file_exists(None)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        check_file_exists(["invalid", "path"])