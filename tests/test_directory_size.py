import os
import pytest
import tempfile
import shutil

from src.directory_size import calculate_directory_size

def test_calculate_directory_size():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with known sizes
        test_files = [
            (os.path.join(temp_dir, 'file1.txt'), 100),
            (os.path.join(temp_dir, 'file2.txt'), 250),
            (os.path.join(temp_dir, 'subdir', 'file3.txt'), 75)
        ]
        
        # Ensure subdirectory exists
        os.makedirs(os.path.dirname(test_files[2][0]), exist_ok=True)
        
        # Create files and write content
        total_expected_size = 0
        for filepath, size in test_files:
            with open(filepath, 'wb') as f:
                f.write(b'0' * size)
            total_expected_size += size
        
        # Test the function
        result = calculate_directory_size(temp_dir)
        assert result == total_expected_size

def test_non_existent_directory():
    # Test that FileNotFoundError is raised for non-existent directory
    with pytest.raises(FileNotFoundError):
        calculate_directory_size('/path/to/non/existent/directory')

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Test that NotADirectoryError is raised when a file is passed
        with pytest.raises(NotADirectoryError):
            calculate_directory_size(temp_file.name)

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test that size is zero for an empty directory
        result = calculate_directory_size(temp_dir)
        assert result == 0