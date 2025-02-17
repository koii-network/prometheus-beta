import os
import pytest
import shutil
import tempfile
from src.directory_utils import delete_directory

def test_delete_directory():
    # Create a temporary directory with some contents
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files and subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('test content')
        with open(os.path.join(temp_dir, 'subdir1', 'file2.txt'), 'w') as f:
            f.write('another test content')
        
        # Call the delete_directory function
        delete_directory(temp_dir)
        
        # Verify directory is deleted
        assert not os.path.exists(temp_dir)

def test_delete_nonexistent_directory():
    # Test deleting a non-existent directory raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        delete_directory('/path/to/nonexistent/directory')

def test_delete_file_instead_of_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        # Try to delete a file using delete_directory
        with pytest.raises(NotADirectoryError):
            delete_directory(temp_file_path)
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)