import os
import pytest
import tempfile
import time
from src.find_oldest_file import find_oldest_file

def test_find_oldest_file():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with controlled creation times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')
        
        # Create files with a small delay to ensure different creation times
        with open(file1_path, 'w') as f:
            f.write('File 1')
        time.sleep(0.1)
        
        with open(file2_path, 'w') as f:
            f.write('File 2')
        time.sleep(0.1)
        
        with open(file3_path, 'w') as f:
            f.write('File 3')
        
        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Verify the result
        assert oldest_file == file1_path

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Verify None is returned for an empty directory
        assert find_oldest_file(temp_dir) is None

def test_invalid_directory():
    # Test invalid directory raises NotADirectoryError
    with pytest.raises(NotADirectoryError):
        find_oldest_file('/path/to/nonexistent/directory')

def test_directory_with_subdirectories():
    # Create a temporary directory with files and subdirectories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file
        file_path = os.path.join(temp_dir, 'testfile.txt')
        with open(file_path, 'w') as f:
            f.write('Test')
        
        # Create a subdirectory
        subdir_path = os.path.join(temp_dir, 'subdir')
        os.makedirs(subdir_path)
        
        # Verify only the file is considered
        oldest_file = find_oldest_file(temp_dir)
        assert oldest_file == file_path