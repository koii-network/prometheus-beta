import os
import pytest
import tempfile
import shutil

from src.file_deletion import delete_file


def test_delete_existing_file():
    """Test deleting an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name
    
    assert os.path.exists(file_path)
    assert delete_file(file_path) is True
    assert not os.path.exists(file_path)


def test_delete_non_existent_file():
    """Test attempting to delete a non-existent file."""
    non_existent_path = "/path/to/non/existent/file.txt"
    
    with pytest.raises(FileNotFoundError):
        delete_file(non_existent_path)


def test_delete_directory():
    """Test attempting to delete a directory."""
    temp_dir = tempfile.mkdtemp()
    
    try:
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)
    finally:
        shutil.rmtree(temp_dir)


def test_delete_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        delete_file(123)
    
    with pytest.raises(TypeError):
        delete_file(None)


def test_delete_file_with_relative_path():
    """Test deleting a file using a relative path."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name
    
    # Get the relative path
    relative_path = os.path.relpath(file_path)
    
    assert os.path.exists(file_path)
    assert delete_file(relative_path) is True
    assert not os.path.exists(file_path)