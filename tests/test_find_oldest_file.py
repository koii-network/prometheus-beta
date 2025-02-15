import os
import pytest
import tempfile
import time
from pathlib import Path
from src.find_oldest_file import find_oldest_file

def test_find_oldest_file_in_temp_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files with different timestamps
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')
        
        # Write files
        with open(file1_path, 'w') as f:
            f.write('file1')
        time.sleep(0.1)  # Ensure different timestamps
        with open(file2_path, 'w') as f:
            f.write('file2')
        time.sleep(0.1)
        with open(file3_path, 'w') as f:
            f.write('file3')
        
        # Find the oldest file
        oldest_file = find_oldest_file(temp_dir)
        
        # Assert the oldest file is returned
        assert oldest_file == file1_path

def test_find_oldest_file_in_current_directory():
    # Use current directory if no directory specified
    current_path = os.path.abspath('.')
    result = find_oldest_file()
    
    # Ensure a file is returned
    assert result is not None
    assert os.path.exists(result)

def test_nonexistent_directory():
    # Test that a nonexistent directory raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        find_oldest_file('/path/that/does/not/exist')

def test_file_instead_of_directory():
    # Test that passing a file instead of a directory raises NotADirectoryError
    temp_file = tempfile.mktemp()
    with open(temp_file, 'w') as f:
        f.write('test')
    
    with pytest.raises(NotADirectoryError):
        find_oldest_file(temp_file)
    
    # Clean up
    os.unlink(temp_file)

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Find oldest file in empty directory
        result = find_oldest_file(temp_dir)
        
        # Expect None to be returned
        assert result is None