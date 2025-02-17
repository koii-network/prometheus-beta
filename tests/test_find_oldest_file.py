import os
import pytest
import tempfile
import time
from src.find_oldest_file import find_oldest_file

def test_find_oldest_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different creation times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')

        # Create first file and wait a bit
        with open(file1_path, 'w') as f:
            f.write('Content 1')
        time.sleep(0.1)

        # Create second file and wait a bit
        with open(file2_path, 'w') as f:
            f.write('Content 2')
        time.sleep(0.1)

        # Create third file
        with open(file3_path, 'w') as f:
            f.write('Content 3')

        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Assert the oldest file is the first file created
        assert oldest_file == file1_path

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Assert None is returned for empty directory
        assert oldest_file is None

def test_invalid_directory():
    # Test with an invalid directory path
    invalid_path = '/path/that/does/not/exist'
    oldest_file = find_oldest_file(invalid_path)
    
    # Assert None is returned for invalid directory
    assert oldest_file is None