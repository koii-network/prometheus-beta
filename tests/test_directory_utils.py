import os
import pytest
import tempfile
from src.directory_utils import list_directory_files

def test_list_directory_files_current_directory():
    # Test listing files in the current directory
    files = list_directory_files('.')
    assert isinstance(files, list)
    # Check that some expected files exist
    expected_files = ['.gitignore', 'README.md', 'requirements.txt']
    for file in expected_files:
        assert file in files

def test_list_directory_files_with_temp_directory():
    # Create a temporary directory with some files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.pdf']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # List files in the temp directory
        listed_files = list_directory_files(temp_dir)
        
        # Check that all created files are listed
        assert set(listed_files) == set(test_files)

def test_list_directory_files_non_existent_directory():
    # Test that FileNotFoundError is raised for non-existent directory
    with pytest.raises(FileNotFoundError):
        list_directory_files('/path/to/non/existent/directory')

def test_list_directory_files_not_a_directory():
    # Test that NotADirectoryError is raised when path is a file
    with pytest.raises(NotADirectoryError):
        list_directory_files('README.md')  # Assuming README.md exists

def test_list_directory_files_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # List files in the empty directory
        listed_files = list_directory_files(temp_dir)
        
        # Check that the list is empty
        assert len(listed_files) == 0