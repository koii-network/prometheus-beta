import os
import pytest
import tempfile
import shutil

from src.directory_size_calculator import calculate_directory_size

def test_calculate_directory_size():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with known sizes
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write('Hello, World!')  # 13 bytes
        
        with open(file2_path, 'w') as f2:
            f2.write('Python Testing')  # 14 bytes
        
        # Calculate total size
        total_size = calculate_directory_size(temp_dir)
        
        # Assert total size matches expected
        assert total_size == 27, f"Expected 27 bytes, got {total_size}"

def test_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        total_size = calculate_directory_size(temp_dir)
        assert total_size == 0, f"Expected 0 bytes for empty directory, got {total_size}"

def test_nested_directory():
    # Create a temporary directory with nested files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory
        nested_dir = os.path.join(temp_dir, 'nested')
        os.makedirs(nested_dir)
        
        # Create files in main and nested directories
        with open(os.path.join(temp_dir, 'main_file.txt'), 'w') as f1:
            f1.write('Main File')  # 9 bytes
        
        with open(os.path.join(nested_dir, 'nested_file.txt'), 'w') as f2:
            f2.write('Nested File')  # 11 bytes
        
        total_size = calculate_directory_size(temp_dir)
        assert total_size == 20, f"Expected 20 bytes, got {total_size}"

def test_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        calculate_directory_size('/path/that/does/not/exist')

def test_not_a_directory():
    # Create a temporary file (not a directory)
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            calculate_directory_size(temp_file.name)