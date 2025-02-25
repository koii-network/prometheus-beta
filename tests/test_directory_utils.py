import os
import pytest
import tempfile
import shutil

from src.directory_utils import delete_empty_directory

def test_delete_empty_directory():
    """Test successful deletion of an empty directory."""
    with tempfile.TemporaryDirectory() as base_dir:
        # Create an empty subdirectory
        empty_dir = os.path.join(base_dir, 'empty_test_dir')
        os.mkdir(empty_dir)
        
        # Verify directory exists before deletion
        assert os.path.exists(empty_dir)
        
        # Delete the empty directory
        result = delete_empty_directory(empty_dir)
        
        # Check deletion was successful
        assert result is True
        assert not os.path.exists(empty_dir)

def test_delete_nonexistent_directory():
    """Test attempting to delete a non-existent directory raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as base_dir:
        non_existent_path = os.path.join(base_dir, 'non_existent_dir')
        
        with pytest.raises(FileNotFoundError):
            delete_empty_directory(non_existent_path)

def test_delete_nonempty_directory():
    """Test attempting to delete a non-empty directory raises OSError."""
    with tempfile.TemporaryDirectory() as base_dir:
        nonempty_dir = os.path.join(base_dir, 'nonempty_test_dir')
        os.mkdir(nonempty_dir)
        
        # Create a file inside the directory
        with open(os.path.join(nonempty_dir, 'test_file.txt'), 'w') as f:
            f.write('test content')
        
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(nonempty_dir)

def test_delete_file_instead_of_directory():
    """Test attempting to delete a file instead of a directory raises ValueError."""
    with tempfile.TemporaryDirectory() as base_dir:
        test_file = os.path.join(base_dir, 'test_file.txt')
        
        # Create a test file
        with open(test_file, 'w') as f:
            f.write('test content')
        
        with pytest.raises(ValueError, match="Path is not a directory"):
            delete_empty_directory(test_file)

def test_delete_with_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        delete_empty_directory(None)
    
    with pytest.raises(TypeError):
        delete_empty_directory(123)

def test_delete_directory_with_trailing_slash():
    """Test deleting a directory with a trailing slash."""
    with tempfile.TemporaryDirectory() as base_dir:
        empty_dir = os.path.join(base_dir, 'empty_test_dir')
        os.mkdir(empty_dir)
        
        # Try deleting with a trailing slash
        result = delete_empty_directory(empty_dir + '/')
        
        assert result is True
        assert not os.path.exists(empty_dir)