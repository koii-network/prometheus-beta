import os
import pytest
import tempfile
import time

from src.most_recent_file import find_most_recent_file

def test_find_most_recent_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with different modification times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')
        
        # Create files
        with open(file1_path, 'w') as f:
            f.write('file1')
        
        # Wait a bit to ensure different modification times
        time.sleep(0.1)
        
        with open(file2_path, 'w') as f:
            f.write('file2')
        
        time.sleep(0.1)
        
        with open(file3_path, 'w') as f:
            f.write('file3')
        
        # Find most recent file
        most_recent = find_most_recent_file(temp_dir)
        
        # Assert the most recent file is file3
        assert most_recent == 'file3.txt'

def test_empty_directory():
    # Create temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Should return None for empty directory
        assert find_most_recent_file(temp_dir) is None

def test_invalid_directory():
    # Test with non-existent directory
    with pytest.raises(ValueError):
        find_most_recent_file('/path/to/nonexistent/directory')

def test_directory_with_subdirectories():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file in the main directory
        main_file = os.path.join(temp_dir, 'main_file.txt')
        with open(main_file, 'w') as f:
            f.write('main file')
        
        # Create a subdirectory with a file
        subdir = os.path.join(temp_dir, 'subdir')
        os.makedirs(subdir)
        sub_file = os.path.join(subdir, 'sub_file.txt')
        with open(sub_file, 'w') as f:
            f.write('sub file')
        
        # The function should only look at files, not enter subdirectories
        most_recent = find_most_recent_file(temp_dir)
        assert most_recent == 'main_file.txt'