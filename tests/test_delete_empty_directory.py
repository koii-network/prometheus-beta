import os
import pytest
import tempfile
import shutil

from src.delete_empty_directory import delete_empty_directory

def test_delete_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        empty_subdir = os.path.join(temp_dir, 'empty_subdir')
        os.makedirs(empty_subdir)
        
        # Test deleting an empty directory
        delete_empty_directory(empty_subdir)
        assert not os.path.exists(empty_subdir)

def test_delete_non_empty_directory_raises_error():
    # Create a temporary directory with a file
    with tempfile.TemporaryDirectory() as temp_dir:
        non_empty_subdir = os.path.join(temp_dir, 'non_empty_subdir')
        os.makedirs(non_empty_subdir)
        
        # Create a file inside the directory
        with open(os.path.join(non_empty_subdir, 'test.txt'), 'w') as f:
            f.write('test')
        
        # Attempt to delete non-empty directory should raise an OSError
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(non_empty_subdir)

def test_delete_non_existent_directory_raises_error():
    # Attempt to delete a non-existent directory should raise FileNotFoundError
    with pytest.raises(FileNotFoundError, match="Directory not found"):
        delete_empty_directory('/path/to/non/existent/directory')

def test_delete_file_instead_of_directory_raises_error():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        # Attempt to delete a file instead of a directory should raise OSError
        with pytest.raises(OSError, match="Path is not a directory"):
            delete_empty_directory(temp_file.name)
        
        # Clean up the temporary file
        os.unlink(temp_file.name)