import os
import pytest
import shutil
import tempfile

from src.directory_utils import delete_directory

def test_delete_directory_normal_case():
    # Create a temporary directory with some files and subdirectories
    with tempfile.TemporaryDirectory() as base_dir:
        # Create some nested directories and files
        os.makedirs(os.path.join(base_dir, 'subdir1', 'subsubdir'))
        os.makedirs(os.path.join(base_dir, 'subdir2'))
        
        # Create some files
        with open(os.path.join(base_dir, 'file1.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(base_dir, 'subdir1', 'file2.txt'), 'w') as f:
            f.write('test')
        
        # Call the delete_directory function
        delete_directory(base_dir)
        
        # Verify the directory is deleted
        assert not os.path.exists(base_dir)

def test_delete_nonexistent_directory():
    # Attempt to delete a non-existent directory should raise FileNotFoundError
    with pytest.raises(FileNotFoundError):
        delete_directory('/path/to/nonexistent/directory')

def test_delete_file_instead_of_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    # Attempt to delete a file should raise ValueError
    with pytest.raises(ValueError):
        delete_directory(temp_file_path)
    
    # Clean up the temporary file
    os.unlink(temp_file_path)

# Note: Testing PermissionError requires special setup and might vary by system,
# so we'll omit that specific test to ensure cross-platform compatibility