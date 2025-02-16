import os
import pytest
import tempfile
import shutil

from src.find_largest_file import find_largest_file

def test_find_largest_file():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different sizes
        file1_path = os.path.join(temp_dir, 'small.txt')
        file2_path = os.path.join(temp_dir, 'large.txt')
        file3_path = os.path.join(temp_dir, 'medium.txt')
        
        # Write content to create different file sizes
        with open(file1_path, 'w') as f:
            f.write('small')
        
        with open(file2_path, 'w') as f:
            f.write('large' * 1000)
        
        with open(file3_path, 'w') as f:
            f.write('medium' * 100)
        
        # Find the largest file
        result = find_largest_file(temp_dir)
        
        # Verify the result
        assert result == file2_path, f"Expected {file2_path}, got {result}"

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test empty directory
        result = find_largest_file(temp_dir)
        assert result is None, "Should return None for empty directory"

def test_invalid_directory():
    with pytest.raises(ValueError, match="Invalid directory"):
        find_largest_file('/path/to/nonexistent/directory')

def test_nested_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory structure
        nested_dir = os.path.join(temp_dir, 'nested')
        os.makedirs(nested_dir)
        
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(nested_dir, 'file2.txt')
        
        with open(file1_path, 'w') as f:
            f.write('small')
        
        with open(file2_path, 'w') as f:
            f.write('large' * 1000)
        
        # Find the largest file
        result = find_largest_file(temp_dir)
        
        # Verify the result includes nested files
        assert result == file2_path, f"Expected {file2_path}, got {result}"