import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories

def test_list_subdirectories_empty_directory():
    """Test listing subdirectories in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert list_subdirectories(temp_dir) == []

def test_list_subdirectories_with_subdirs():
    """Test listing subdirectories with multiple subdirs."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))
        
        # Create a file to ensure it's not included
        with open(os.path.join(temp_dir, 'testfile.txt'), 'w') as f:
            f.write('test')
        
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Check result
        assert set(subdirs) == {'subdir1', 'subdir2', 'subdir3'}

def test_list_subdirectories_nonexistent_path():
    """Test raising FileNotFoundError for nonexistent path."""
    with pytest.raises(FileNotFoundError):
        list_subdirectories('/path/that/does/not/exist')

def test_list_subdirectories_not_a_directory():
    """Test raising ValueError when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError):
            list_subdirectories(temp_file.name)

def test_list_subdirectories_nested_subdirs():
    """Test that only immediate subdirectories are returned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1', 'nested'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Check result
        assert set(subdirs) == {'subdir1', 'subdir2'}