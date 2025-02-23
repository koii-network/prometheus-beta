import os
import pytest
import tempfile
import shutil

from src.delete_empty_directory import delete_empty_directory

def test_delete_empty_directory():
    """Test deleting an empty directory."""
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a subdirectory to test
        empty_dir = os.path.join(temp_dir, 'empty_subdir')
        os.mkdir(empty_dir)

        # Test deletion of empty directory
        assert delete_empty_directory(empty_dir) == True
        assert not os.path.exists(empty_dir)

def test_delete_nonexistent_directory():
    """Test attempting to delete a non-existent directory."""
    with pytest.raises(FileNotFoundError):
        delete_empty_directory('/path/to/nonexistent/directory')

def test_delete_directory_with_contents():
    """Test attempting to delete a non-empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a non-empty directory
        non_empty_dir = os.path.join(temp_dir, 'non_empty_dir')
        os.mkdir(non_empty_dir)
        
        # Create a file inside the directory
        with open(os.path.join(non_empty_dir, 'test_file.txt'), 'w') as f:
            f.write('test')

        # Test that deleting fails
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(non_empty_dir)

def test_delete_file_instead_of_directory():
    """Test attempting to delete a file instead of a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file
        test_file = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file, 'w') as f:
            f.write('test')

        # Test that deleting fails
        with pytest.raises(OSError, match="Path is not a directory"):
            delete_empty_directory(test_file)

def test_delete_empty_directory_with_none_or_empty_path():
    """Test handling of None or empty path."""
    with pytest.raises(ValueError):
        delete_empty_directory(None)
    
    with pytest.raises(ValueError):
        delete_empty_directory('')