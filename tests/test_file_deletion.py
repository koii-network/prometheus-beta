import os
import pytest
import tempfile
from src.file_deletion import delete_file

def test_delete_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Verify the file exists before deletion
    assert os.path.exists(temp_path)
    
    # Delete the file
    delete_file(temp_path)
    
    # Verify the file no longer exists
    assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    # Should raise FileNotFoundError for non-existent file
    with pytest.raises(FileNotFoundError):
        delete_file('non_existent_file.txt')

def test_delete_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Should raise IsADirectoryError when trying to delete a directory
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)

# Note: Testing PermissionError is tricky and environment-dependent, 
# so we'll omit that for now