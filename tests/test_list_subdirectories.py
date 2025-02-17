import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories

def test_list_subdirectories():
    # Create a temporary directory with some subdirectories for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))
        
        # Create a file to ensure it's not included
        with open(os.path.join(temp_dir, 'test_file.txt'), 'w') as f:
            f.write('test')
        
        # Test the function
        result = list_subdirectories(temp_dir)
        
        # Check results
        assert len(result) == 3
        assert set(result) == {'subdir1', 'subdir2', 'subdir3'}

def test_empty_directory():
    # Test with an empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        result = list_subdirectories(temp_dir)
        assert result == []

def test_nonexistent_directory():
    # Test with a nonexistent directory
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file and test
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            list_subdirectories(temp_file.name)