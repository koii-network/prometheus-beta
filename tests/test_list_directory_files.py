import os
import pytest
import tempfile
from src.list_directory_files import list_directory_files

def test_list_directory_files_current_directory():
    """Test listing files in the current directory."""
    files = list_directory_files()
    assert isinstance(files, list)
    # Check for known files in the repository
    expected_files = ['.gitignore', 'README.md', 'requirements.txt']
    for file in expected_files:
        assert file in files

def test_list_directory_files_with_temp_directory():
    """Test listing files in a temporary directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # List files in the temporary directory
        listed_files = list_directory_files(temp_dir)
        assert set(listed_files) == set(test_files)

def test_list_directory_files_with_non_existent_directory():
    """Test that an error is raised for a non-existent directory."""
    with pytest.raises(FileNotFoundError):
        list_directory_files('/path/to/non/existent/directory')

def test_list_directory_files_with_file_instead_of_directory():
    """Test that an error is raised when a file path is provided instead of a directory."""
    with pytest.raises(NotADirectoryError):
        list_directory_files('README.md')

def test_list_directory_files_ignores_subdirectories():
    """Test that subdirectories are not included in the file list."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files and a subdirectory
        test_files = ['file1.txt', 'file2.txt']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        # List files in the temporary directory
        listed_files = list_directory_files(temp_dir)
        assert set(listed_files) == set(test_files)
        assert 'subdir' not in listed_files