import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories

def test_list_subdirectories():
    # Create a temporary directory with some test subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))
        
        # Create a test file (not a directory)
        with open(os.path.join(temp_dir, 'testfile.txt'), 'w') as f:
            f.write('test')
        
        # Test listing subdirectories
        result = list_subdirectories(temp_dir)
        
        # Assert expected results
        assert set(result) == {'subdir1', 'subdir2', 'subdir3'}
        assert 'testfile.txt' not in result

def test_empty_directory():
    # Create an empty temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        result = list_subdirectories(temp_dir)
        assert result == []

def test_nonexistent_directory():
    # Test with a nonexistent directory
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            list_subdirectories(temp_file.name)