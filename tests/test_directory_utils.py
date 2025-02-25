import os
import pytest
import shutil
import tempfile

from src.directory_utils import delete_directory

def test_delete_directory_success():
    """Test successful directory deletion."""
    # Create a temporary directory with some files and subdirectories
    with tempfile.TemporaryDirectory() as base_dir:
        # Create nested directories and files
        sub_dir1 = os.path.join(base_dir, 'subdir1')
        sub_dir2 = os.path.join(sub_dir1, 'subdir2')
        os.makedirs(sub_dir2)
        
        # Create some files
        with open(os.path.join(base_dir, 'file1.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(sub_dir1, 'file2.txt'), 'w') as f:
            f.write('test')
        
        # Attempt to delete the directory
        result = delete_directory(base_dir)
        
        # Verify directory is deleted and function returns True
        assert result is True
        assert not os.path.exists(base_dir)

def test_delete_nonexistent_directory():
    """Test that FileNotFoundError is raised for nonexistent directory."""
    with tempfile.TemporaryDirectory() as base_dir:
        nonexistent_dir = os.path.join(base_dir, 'nonexistent')
        with pytest.raises(FileNotFoundError):
            delete_directory(nonexistent_dir)

def test_delete_file_instead_of_directory():
    """Test that ValueError is raised when trying to delete a file."""
    with tempfile.TemporaryDirectory() as base_dir:
        test_file = os.path.join(base_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        
        with pytest.raises(ValueError):
            delete_directory(test_file)

def test_delete_relative_path():
    """Test deleting a directory using a relative path."""
    with tempfile.TemporaryDirectory() as base_dir:
        # Change current working directory
        original_cwd = os.getcwd()
        os.chdir(base_dir)
        
        try:
            # Create a nested directory structure
            os.makedirs('test_dir/nested_dir')
            with open('test_dir/file.txt', 'w') as f:
                f.write('test')
            
            # Delete using relative path
            result = delete_directory('test_dir')
            
            # Verify directory is deleted and function returns True
            assert result is True
            assert not os.path.exists('test_dir')
        finally:
            # Restore original working directory
            os.chdir(original_cwd)

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError):
        delete_directory(123)  # Integer input
    with pytest.raises(TypeError):
        delete_directory(None)  # None input