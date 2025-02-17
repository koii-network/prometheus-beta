import os
import pytest
import tempfile
import shutil

from src.delete_empty_directory import delete_empty_directory

def test_delete_empty_directory():
    # Create a temporary empty directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test successful deletion of empty directory
        delete_empty_directory(temp_dir)
        assert not os.path.exists(temp_dir)
    finally:
        # Cleanup in case of test failure
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)

def test_delete_non_empty_directory():
    # Create a temporary directory with a file
    temp_dir = tempfile.mkdtemp()
    temp_file = os.path.join(temp_dir, 'test.txt')
    
    try:
        with open(temp_file, 'w') as f:
            f.write('test')
        
        # Should raise OSError for non-empty directory
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(temp_dir)
    finally:
        # Cleanup
        shutil.rmtree(temp_dir, ignore_errors=True)

def test_delete_non_existent_directory():
    # Test deleting a non-existent directory
    with pytest.raises(FileNotFoundError, match="Directory not found"):
        delete_empty_directory('/path/to/non/existent/directory')

def test_delete_file_instead_of_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Should raise OSError for files
        with pytest.raises(OSError, match="Path is not a directory"):
            delete_empty_directory(temp_file_path)
    finally:
        # Cleanup
        os.unlink(temp_file_path)