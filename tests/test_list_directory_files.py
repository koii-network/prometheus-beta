import os
import pytest
import tempfile
import shutil

from src.list_directory_files import list_directory_files

def test_list_directory_files_current_directory():
    """Test listing files in the current directory."""
    files = list_directory_files('.')
    assert isinstance(files, list)
    assert all(isinstance(f, str) for f in files)

def test_list_directory_files_with_temp_directory():
    """Test listing files in a temporary directory."""
    # Create a temporary directory with some test files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.log']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory to ensure only files are returned
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        # List files
        files = list_directory_files(temp_dir)
        
        # Check results
        assert set(files) == set(test_files)

def test_list_directory_files_non_existent_directory():
    """Test that an exception is raised for non-existent directory."""
    with pytest.raises(FileNotFoundError):
        list_directory_files('/path/to/non/existent/directory')

def test_list_directory_files_not_a_directory():
    """Test that an exception is raised if path is not a directory."""
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        try:
            with pytest.raises(NotADirectoryError):
                list_directory_files(temp_file.name)
        finally:
            # Clean up the temporary file
            os.unlink(temp_file.name)