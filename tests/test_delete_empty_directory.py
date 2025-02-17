import os
import pytest
import tempfile
import shutil

from src.delete_empty_directory import delete_empty_directory

def test_delete_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        empty_dir = os.path.join(temp_dir, 'empty_dir')
        os.mkdir(empty_dir)
        
        # Test successful deletion
        assert delete_empty_directory(empty_dir) == True
        assert not os.path.exists(empty_dir)

def test_delete_nonexistent_directory():
    # Test deleting a non-existent directory
    with pytest.raises(FileNotFoundError):
        delete_empty_directory('/path/to/nonexistent/directory')

def test_delete_nonempty_directory():
    # Create a temporary directory with a file
    with tempfile.TemporaryDirectory() as temp_dir:
        nonempty_dir = os.path.join(temp_dir, 'nonempty_dir')
        os.mkdir(nonempty_dir)
        
        # Add a file to make the directory non-empty
        with open(os.path.join(nonempty_dir, 'dummy.txt'), 'w') as f:
            f.write('test')
        
        # Test that deletion fails for non-empty directory
        with pytest.raises(OSError):
            delete_empty_directory(nonempty_dir)

def test_delete_file_instead_of_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Test that trying to delete a file raises an OSError
        with pytest.raises(OSError):
            delete_empty_directory(temp_file_path)
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)