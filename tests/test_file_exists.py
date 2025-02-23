import os
import pytest
import tempfile

from src.file_exists import file_exists

def test_existing_file():
    """Test that the function returns True for an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert file_exists(temp_file_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_non_existing_file():
    """Test that the function returns False for a non-existing file."""
    non_existent_path = "/path/to/definitely/non/existing/file.txt"
    assert file_exists(non_existent_path) is False

def test_directory():
    """Test that the function returns False for a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert file_exists(temp_dir) is False

def test_invalid_input_type():
    """Test that the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(123)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(None)

def test_empty_string():
    """Test handling of an empty string path."""
    assert file_exists("") is False

def test_relative_path():
    """Test handling of relative file paths."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
        relative_path = os.path.relpath(temp_file_path)
    
    try:
        assert file_exists(relative_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_path_with_spaces():
    """Test handling of file paths with spaces."""
    with tempfile.NamedTemporaryFile(delete=False, prefix="test file ") as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert file_exists(temp_file_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)