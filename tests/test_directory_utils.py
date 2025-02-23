import os
import pytest
import tempfile
import shutil

from src.directory_utils import list_subdirectories


def test_list_subdirectories_normal_case():
    """Test listing subdirectories in a typical scenario."""
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
        
        # Assert
        assert set(subdirs) == {'subdir1', 'subdir2', 'subdir3'}
        assert len(subdirs) == 3


def test_list_subdirectories_empty_directory():
    """Test listing subdirectories in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        subdirs = list_subdirectories(temp_dir)
        assert subdirs == []


def test_list_subdirectories_nonexistent_directory():
    """Test that FileNotFoundError is raised for a nonexistent directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        nonexistent_path = os.path.join(temp_dir, 'nonexistent_dir')
        
        with pytest.raises(FileNotFoundError):
            list_subdirectories(nonexistent_path)


def test_list_subdirectories_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file
        test_file = os.path.join(temp_dir, 'testfile.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        
        with pytest.raises(NotADirectoryError):
            list_subdirectories(test_file)


def test_list_subdirectories_sorted():
    """Test that subdirectories are returned in sorted order."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create subdirectories out of alphabetical order
        os.makedirs(os.path.join(temp_dir, 'subdir_c'))
        os.makedirs(os.path.join(temp_dir, 'subdir_a'))
        os.makedirs(os.path.join(temp_dir, 'subdir_b'))

        subdirs = list_subdirectories(temp_dir)
        
        # Assert they are in sorted order
        assert subdirs == ['subdir_a', 'subdir_b', 'subdir_c']