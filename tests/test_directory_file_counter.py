import os
import pytest
import tempfile
import shutil

from src.directory_file_counter import count_files_in_directory

def test_count_files_in_directory():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.py']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Test that the function returns the correct number of files
        assert count_files_in_directory(temp_dir) == 3

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test that an empty directory returns 0 files
        assert count_files_in_directory(temp_dir) == 0

def test_nonexistent_directory():
    # Test that a nonexistent directory raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        count_files_in_directory('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file (not a directory)
    with tempfile.NamedTemporaryFile() as temp_file:
        # Test that trying to count files in a file raises NotADirectoryError
        with pytest.raises(NotADirectoryError):
            count_files_in_directory(temp_file.name)

def test_directory_with_subdirectories():
    # Create a temporary directory with files and subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        test_files = ['file1.txt', 'file2.txt']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory with a file
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'subdir', 'subfile.txt'), 'w') as f:
            f.write('test content')
        
        # Test that only files in the root directory are counted
        assert count_files_in_directory(temp_dir) == 2