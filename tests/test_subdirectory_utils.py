import os
import pytest
import tempfile
import shutil

from src.subdirectory_utils import list_subdirectories

def test_list_subdirectories():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'nested', 'subdir3'))
        
        # Create a file to ensure it's not included
        with open(os.path.join(temp_dir, 'testfile.txt'), 'w') as f:
            f.write('test')
        
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Check number and paths of subdirectories
        assert len(subdirs) == 3
        assert os.path.join(temp_dir, 'subdir1') in subdirs
        assert os.path.join(temp_dir, 'subdir2') in subdirs
        assert os.path.join(temp_dir, 'nested') in subdirs

def test_nonexistent_directory():
    # Test behavior with a non-existent directory
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Test with a file instead of a directory
        with pytest.raises(NotADirectoryError):
            list_subdirectories(temp_file.name)

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Check that no subdirectories are returned
        assert len(subdirs) == 0