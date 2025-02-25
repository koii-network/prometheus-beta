import os
import pytest
import tempfile
from src.file_size import get_file_size

def test_get_file_size_normal():
    """Test getting size of a normal file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Hello, World!")
        temp_file.close()
        
        try:
            file_size = get_file_size(temp_file.name)
            assert file_size == 13, f"Expected file size 13, got {file_size}"
        finally:
            os.unlink(temp_file.name)

def test_get_file_size_empty_file():
    """Test getting size of an empty file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()
        
        try:
            file_size = get_file_size(temp_file.name)
            assert file_size == 0, f"Expected file size 0, got {file_size}"
        finally:
            os.unlink(temp_file.name)

def test_get_file_size_nonexistent_file():
    """Test handling of nonexistent file."""
    with pytest.raises(FileNotFoundError):
        get_file_size("/path/to/nonexistent/file.txt")

def test_get_file_size_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        get_file_size(123)
    with pytest.raises(TypeError):
        get_file_size(None)

def test_get_file_size_directory():
    """Test handling of directory path."""
    with pytest.raises(IsADirectoryError):
        get_file_size(os.path.dirname(os.path.abspath(__file__)))