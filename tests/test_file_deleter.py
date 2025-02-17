import os
import pytest
import tempfile
from src.file_deleter import delete_file

def test_delete_existing_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Ensure the file exists before deletion
    assert os.path.exists(temp_path)
    
    # Delete the file
    delete_file(temp_path)
    
    # Verify the file is deleted
    assert not os.path.exists(temp_path)

def test_delete_nonexistent_file():
    # Create a path that doesn't exist
    non_existent_path = os.path.join(tempfile.gettempdir(), 'nonexistent_file_test.txt')
    
    # Verify FileNotFoundError is raised
    with pytest.raises(FileNotFoundError):
        delete_file(non_existent_path)

def test_delete_directory():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Verify IsADirectoryError is raised
    with pytest.raises(IsADirectoryError):
        delete_file(temp_dir)

def test_delete_file_without_permission(monkeypatch):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Simulate permission error by mocking os.remove
    def mock_remove(path):
        raise PermissionError("Simulated permission error")
    
    monkeypatch.setattr(os, 'remove', mock_remove)
    
    # Verify PermissionError is raised
    with pytest.raises(PermissionError):
        delete_file(temp_path)