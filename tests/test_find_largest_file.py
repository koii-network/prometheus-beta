import os
import pytest
import tempfile
import shutil
from src.find_largest_file import find_largest_file

def test_find_largest_file():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with different sizes
        file1 = os.path.join(temp_dir, 'small.txt')
        file2 = os.path.join(temp_dir, 'large.txt')
        file3 = os.path.join(temp_dir, 'medium.txt')
        
        # Write content to create files of different sizes
        with open(file1, 'w') as f:
            f.write('small')  # 5 bytes
        
        with open(file2, 'w') as f:
            f.write('this is a large file content' * 10)  # 270 bytes
        
        with open(file3, 'w') as f:
            f.write('medium file' * 5)  # 55 bytes
        
        # Find the largest file
        result = find_largest_file(temp_dir)
        
        # Assert that the largest file is correctly identified
        assert result == file2

def test_empty_directory():
    # Test with an empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        result = find_largest_file(temp_dir)
        assert result is None

def test_invalid_directory():
    # Test with an invalid directory path
    result = find_largest_file('/path/that/does/not/exist')
    assert result is None

def test_directory_with_subdirectories():
    # Create a temporary directory with files and subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files in the main directory
        file1 = os.path.join(temp_dir, 'file1.txt')
        file2 = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1, 'w') as f:
            f.write('small')  # 5 bytes
        
        with open(file2, 'w') as f:
            f.write('this is a large file content' * 10)  # 270 bytes
        
        # Create a subdirectory with a file
        subdir = os.path.join(temp_dir, 'subdir')
        os.makedirs(subdir)
        subfile = os.path.join(subdir, 'subfile.txt')
        
        with open(subfile, 'w') as f:
            f.write('medium file' * 5)  # 55 bytes
        
        # Find the largest file
        result = find_largest_file(temp_dir)
        
        # Assert that the largest file is correctly identified
        assert result == file2