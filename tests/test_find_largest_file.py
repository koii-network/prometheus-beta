import os
import pytest
import tempfile
import pathlib
from src.find_largest_file import find_largest_file

def test_find_largest_file():
    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with different sizes
        files = [
            ('small.txt', 10),
            ('medium.txt', 100),
            ('large.txt', 1000)
        ]
        
        for filename, size in files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(b'0' * size)
        
        # Find the largest file
        largest_file = find_largest_file(temp_dir)
        assert largest_file == os.path.join(temp_dir, 'large.txt')

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test empty directory
        result = find_largest_file(temp_dir)
        assert result is None

def test_nonexistent_directory():
    # Test non-existent directory
    with pytest.raises(ValueError, match="Directory does not exist"):
        find_largest_file('/path/to/nonexistent/directory')

def test_not_a_directory():
    # Create a temporary file to test
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError, match="Path is not a directory"):
            find_largest_file(temp_file.name)