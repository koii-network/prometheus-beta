import os
import pytest
import tempfile
import shutil

from src.directory_utils import list_files

def test_list_files_normal_case():
    """Test listing files in a normal directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.jpg', 'file3.pdf']
        for filename in test_files:
            open(os.path.join(temp_dir, filename), 'w').close()
        
        # Also create a subdirectory to ensure it's not included
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        # Get list of files
        files = list_files(temp_dir)
        
        # Check that only files are returned
        assert set(files) == set(test_files)
        assert len(files) == 3

def test_empty_directory():
    """Test listing files in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        files = list_files(temp_dir)
        assert files == []

def test_nonexistent_directory():
    """Test that FileNotFoundError is raised for nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        list_files('/path/to/nonexistent/directory')

def test_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            list_files(temp_file.name)

def test_user_path_expansion():
    """Test that user path expansion works correctly."""
    home_dir_files = list_files('~')
    assert isinstance(home_dir_files, list)
    # Ensure it doesn't raise an error and returns a list