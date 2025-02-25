import os
import pytest
import tempfile
import pathlib
from src.file_operations import delete_file

def test_delete_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Verify file exists before deletion
    assert os.path.exists(temp_path)
    
    # Delete the file
    result = delete_file(temp_path)
    
    # Verify file is deleted
    assert result is True
    assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    # Test deleting a file that doesn't exist
    non_existent_path = "/path/to/nonexistent/file.txt"
    
    with pytest.raises(FileNotFoundError):
        delete_file(non_existent_path)

def test_delete_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test attempting to delete a directory
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)

def test_delete_empty_path():
    # Test empty path
    with pytest.raises(ValueError):
        delete_file("")
    
    with pytest.raises(ValueError):
        delete_file(None)

def test_delete_path_with_special_characters():
    # Create a temporary file with special characters
    with tempfile.NamedTemporaryFile(prefix="test file !@#$%^&*()", delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Verify file exists before deletion
    assert os.path.exists(temp_path)
    
    # Delete the file
    result = delete_file(temp_path)
    
    # Verify file is deleted
    assert result is True
    assert not os.path.exists(temp_path)