import os
import pytest
import tempfile
import shutil
from src.list_subdirectories import list_subdirectories

def test_list_subdirectories():
    # Create a temporary directory with some subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create subdirectories
        subdir1 = os.path.join(temp_dir, 'subdir1')
        subdir2 = os.path.join(temp_dir, 'subdir2')
        os.makedirs(subdir1)
        os.makedirs(subdir2)
        
        # Create a file to ensure only directories are returned
        with open(os.path.join(temp_dir, 'file.txt'), 'w') as f:
            f.write('test')
        
        # Test the function
        result = list_subdirectories(temp_dir)
        
        # Check results
        assert len(result) == 2
        assert subdir1 in result
        assert subdir2 in result

def test_nonexistent_directory():
    # Test with a nonexistent directory
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Test with a file path instead of a directory
        with pytest.raises(NotADirectoryError):
            list_subdirectories(temp_file.name)

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        result = list_subdirectories(temp_dir)
        assert len(result) == 0