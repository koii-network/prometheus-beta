import os
import pytest
import tempfile

from src.file_utils import file_exists

def test_file_exists_with_existing_file():
    """Test that file_exists returns True for an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert file_exists(temp_file_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_file_exists_with_nonexistent_file():
    """Test that file_exists returns False for a nonexistent file."""
    assert file_exists("/path/to/nonexistent/file.txt") is False

def test_file_exists_with_directory():
    """Test that file_exists returns False for a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert file_exists(temp_dir) is False

def test_file_exists_with_invalid_input():
    """Test that file_exists raises TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        file_exists(123)
    
    with pytest.raises(TypeError, match="file_path must be a string"):
        file_exists(None)

def test_file_exists_with_empty_string():
    """Test that file_exists handles empty string input."""
    assert file_exists("") is False

def test_file_exists_with_whitespace_string():
    """Test that file_exists handles whitespace string input."""
    assert file_exists("   ") is False