import os
import pytest
import tempfile
import shutil

from src.list_subdirectories import list_subdirectories


def test_list_subdirectories_normal_case():
    """Test listing subdirectories in a typical scenario."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        os.makedirs(os.path.join(temp_dir, 'subdir3'))
        
        # Create a file to ensure it's not included
        with open(os.path.join(temp_dir, 'testfile.txt'), 'w') as f:
            f.write('test')
        
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Assert expected results
        assert set(subdirs) == {'subdir1', 'subdir2', 'subdir3'}
        assert len(subdirs) == 3


def test_empty_directory():
    """Test listing subdirectories in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Get subdirectories
        subdirs = list_subdirectories(temp_dir)
        
        # Assert no subdirectories
        assert subdirs == []


def test_nonexistent_directory():
    """Test attempting to list subdirectories in a nonexistent directory."""
    with tempfile.TemporaryDirectory() as parent_dir:
        nonexistent_dir = os.path.join(parent_dir, 'nonexistent_dir')
        
        # Expect FileNotFoundError
        with pytest.raises(FileNotFoundError):
            list_subdirectories(nonexistent_dir)


def test_not_a_directory():
    """Test attempting to list subdirectories on a file instead of a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file
        test_file = os.path.join(temp_dir, 'testfile.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        
        # Expect NotADirectoryError
        with pytest.raises(NotADirectoryError):
            list_subdirectories(test_file)