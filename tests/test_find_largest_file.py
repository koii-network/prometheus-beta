import os
import pytest
import tempfile
import shutil

from src.find_largest_file import find_largest_file

def test_find_largest_file():
    """
    Test finding the largest file in a directory.
    """
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different sizes
        files = [
            ('small.txt', 100),
            ('medium.txt', 500),
            ('large.txt', 1000)
        ]
        
        # Write files with specified sizes
        for filename, size in files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(b'0' * size)
        
        # Find largest file
        largest_file, largest_size = find_largest_file(temp_dir)
        
        # Assert the largest file is correctly identified
        assert os.path.basename(largest_file) == 'large.txt'
        assert largest_size == 1000

def test_empty_directory():
    """
    Test behavior with an empty directory.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        largest_file, largest_size = find_largest_file(temp_dir)
        
        assert largest_file is None
        assert largest_size == 0

def test_nonexistent_directory():
    """
    Test error handling for nonexistent directory.
    """
    with pytest.raises(FileNotFoundError):
        find_largest_file('/path/to/nonexistent/directory')

def test_not_a_directory():
    """
    Test error handling when path is not a directory.
    """
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            find_largest_file(temp_file.name)

def test_directory_with_subdirectories():
    """
    Test finding largest file when directory contains subdirectories.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files and a subdirectory
        files = [
            ('file1.txt', 100),
            ('file2.txt', 500)
        ]
        
        # Write files with specified sizes
        for filename, size in files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(b'0' * size)
        
        # Create a subdirectory with a file
        subdir = os.path.join(temp_dir, 'subdir')
        os.makedirs(subdir)
        large_subfile = os.path.join(subdir, 'large_subfile.txt')
        with open(large_subfile, 'wb') as f:
            f.write(b'0' * 250)
        
        # Find largest file
        largest_file, largest_size = find_largest_file(temp_dir)
        
        # Assert the largest file is correctly identified
        assert os.path.basename(largest_file) == 'file2.txt'
        assert largest_size == 500