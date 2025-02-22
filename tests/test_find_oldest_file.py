import os
import pytest
import tempfile
import time
from src.find_oldest_file import find_oldest_file

def test_find_oldest_file():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different creation times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')
        
        # Create file1 first
        with open(file1_path, 'w') as f:
            f.write('File 1')
        time.sleep(0.1)  # Small delay to ensure different creation times
        
        # Create file2
        with open(file2_path, 'w') as f:
            f.write('File 2')
        time.sleep(0.1)
        
        # Create file3
        with open(file3_path, 'w') as f:
            f.write('File 3')
        
        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Assert that file1 is the oldest
        assert oldest_file == file1_path

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Expect None when directory is empty
        assert find_oldest_file(temp_dir) is None

def test_nonexistent_directory():
    # Expect FileNotFoundError for non-existent directory
    with pytest.raises(FileNotFoundError):
        find_oldest_file('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Expect NotADirectoryError when path is not a directory
        with pytest.raises(NotADirectoryError):
            find_oldest_file(temp_file.name)