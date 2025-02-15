import os
import pytest
import tempfile
from src.largest_file_finder import find_largest_file

def test_find_largest_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different sizes
        files = [
            ('small.txt', 10),
            ('medium.txt', 100),
            ('large.txt', 1000)
        ]
        
        # Write files with specified sizes
        for filename, size in files:
            filepath = os.path.join(temp_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(b'0' * size)
        
        # Find largest file
        largest = find_largest_file(temp_dir)
        
        # Verify the largest file is correctly identified
        assert largest == os.path.join(temp_dir, 'large.txt')

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Empty directory should return None
        assert find_largest_file(temp_dir) is None

def test_non_existent_directory():
    # Non-existent directory should return None
    assert find_largest_file('/path/to/non/existent/directory') is None

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Attempting to search a file should raise NotADirectoryError
        with pytest.raises(NotADirectoryError):
            find_largest_file(temp_file.name)

def test_directory_with_subdirectories_and_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create both files and subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        
        files = [
            ('file1.txt', 50),
            ('file2.txt', 150),
            ('file3.txt', 100)
        ]
        
        for filename, size in files:
            filepath = os.path.join(temp_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(b'0' * size)
        
        # Find largest file
        largest = find_largest_file(temp_dir)
        
        # Verify the largest file is correctly identified
        assert largest == os.path.join(temp_dir, 'file2.txt')