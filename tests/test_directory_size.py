import os
import pytest
import tempfile
import shutil

from src.directory_size import calculate_directory_total_size

def test_calculate_directory_total_size():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with known sizes
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('Hello' * 100)  # 500 bytes
        
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
            f.write('World' * 200)  # 1000 bytes
        
        # Nested directory
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'subdir', 'file3.txt'), 'w') as f:
            f.write('Test' * 150)  # 600 bytes
        
        # Calculate total size
        total_size = calculate_directory_total_size(temp_dir)
        
        # Expected total size: 500 + 1000 + 600 = 2100 bytes
        assert total_size == 2100

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        total_size = calculate_directory_total_size(temp_dir)
        assert total_size == 0

def test_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        calculate_directory_total_size('/path/to/non/existent/directory')

def test_not_a_directory():
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            calculate_directory_total_size(temp_file.name)