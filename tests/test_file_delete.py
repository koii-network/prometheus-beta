import os
import pytest
import tempfile
from src.file_delete import delete_file

def test_delete_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Verify file exists before deletion
    assert os.path.exists(temp_path)
    
    # Delete the file
    delete_file(temp_path)
    
    # Verify file is deleted
    assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    # Try to delete a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        delete_file('nonexistent_file.txt')

def test_delete_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Try to delete a directory (should raise IsADirectoryError)
        with pytest.raises(IsADirectoryError):
            delete_file(temp_dir)

def test_delete_no_permission(monkeypatch):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Modify file permissions to simulate permission error
    os.chmod(temp_path, 0o444)  # Read-only
    
    # Try to delete file without write permissions
    with pytest.raises(PermissionError):
        delete_file(temp_path)
    
    # Clean up: restore permissions and remove file
    os.chmod(temp_path, 0o666)
    os.unlink(temp_path)