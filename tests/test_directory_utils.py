import os
import pytest
import shutil
import tempfile

from src.directory_utils import delete_directory

def test_delete_directory_success():
    """Test successful directory deletion."""
    # Create a temporary directory with some files and subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some nested files and directories
        os.makedirs(os.path.join(temp_dir, 'subdir1', 'subsubdir'))
        open(os.path.join(temp_dir, 'file1.txt'), 'w').close()
        open(os.path.join(temp_dir, 'subdir1', 'file2.txt'), 'w').close()
        
        # Attempt to delete the directory
        delete_directory(temp_dir)
        
        # Verify the directory no longer exists
        assert not os.path.exists(temp_dir)

def test_delete_nonexistent_directory():
    """Test that FileNotFoundError is raised for non-existent directory."""
    with pytest.raises(FileNotFoundError):
        delete_directory('/path/to/nonexistent/directory')

def test_delete_file_instead_of_directory():
    """Test that ValueError is raised when trying to delete a file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError, match="is not a directory"):
            delete_directory(temp_file_path)
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

def test_delete_readonly_directory():
    """Test that directory can still be deleted even with read-only permissions."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files in the directory
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        open(os.path.join(temp_dir, 'file.txt'), 'w').close()
        
        # Make the directory and its contents read-only
        os.chmod(temp_dir, 0o555)
        os.chmod(os.path.join(temp_dir, 'subdir'), 0o555)
        os.chmod(os.path.join(temp_dir, 'file.txt'), 0o444)
        
        # Attempt to delete the directory (should succeed by changing permissions)
        delete_directory(temp_dir)
        
        # Verify the directory is gone
        assert not os.path.exists(temp_dir)