import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories

def test_list_subdirectories():
    # Create a temporary directory with some test subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))
        
        # Create a file to ensure it's not included
        with open(os.path.join(temp_dir, 'testfile.txt'), 'w') as f:
            f.write('test')
        
        # Test the function
        result = list_subdirectories(temp_dir)
        
        # Check that only subdirectories are returned
        assert set(result) == {'subdir1', 'subdir2', 'subdir3'}
        assert len(result) == 3

def test_nonexistent_directory():
    # Test that FileNotFoundError is raised for non-existent directory
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Test that NotADirectoryError is raised when path is a file
        with pytest.raises(NotADirectoryError):
            list_subdirectories(temp_file.name)

def test_empty_directory():
    # Create an empty temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test that an empty list is returned
        result = list_subdirectories(temp_dir)
        assert result == []