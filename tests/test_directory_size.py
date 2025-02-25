import os
import pytest
import tempfile
from src.directory_size import calculate_directory_size

def test_calculate_directory_size():
    # Create a temporary directory with test files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with known sizes
        test_files = [
            ('file1.txt', 100),
            ('file2.txt', 200),
            ('subdir/file3.txt', 300)
        ]
        
        # Create the files
        total_expected_size = 0
        for file_path, size in test_files:
            full_path = os.path.join(temp_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, 'wb') as f:
                f.write(b'0' * size)
            total_expected_size += size
        
        # Calculate directory size
        calculated_size = calculate_directory_size(temp_dir)
        
        # Assert the calculated size matches expected size
        assert calculated_size == total_expected_size

def test_calculate_directory_size_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Size of empty directory should be 0
        assert calculate_directory_size(temp_dir) == 0

def test_calculate_directory_size_nonexistent_directory():
    # Test that FileNotFoundError is raised for non-existent directory
    with pytest.raises(FileNotFoundError):
        calculate_directory_size('/path/to/nonexistent/directory')

def test_calculate_directory_size_not_a_directory():
    # Create a temporary file (not a directory)
    with tempfile.NamedTemporaryFile() as temp_file:
        # Test that NotADirectoryError is raised
        with pytest.raises(NotADirectoryError):
            calculate_directory_size(temp_file.name)