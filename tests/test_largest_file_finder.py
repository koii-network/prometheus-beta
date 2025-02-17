import os
import pytest
import tempfile
import pathlib
from src.largest_file_finder import find_largest_file

def test_find_largest_file_basic():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files with different sizes
        file1_path = os.path.join(tmpdir, 'small.txt')
        file2_path = os.path.join(tmpdir, 'large.txt')
        
        with open(file1_path, 'w') as f:
            f.write('small')
        
        with open(file2_path, 'w') as f:
            f.write('large' * 100)
        
        # Find largest file
        result_path, result_size = find_largest_file(tmpdir)
        
        assert result_path == file2_path
        assert result_size == len('large' * 100)

def test_find_largest_file_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Test empty directory
        result_path, result_size = find_largest_file(tmpdir)
        
        assert result_path is None
        assert result_size == 0

def test_find_largest_file_invalid_directory():
    with pytest.raises(ValueError, match="Directory does not exist"):
        find_largest_file('/nonexistent/path')

def test_find_largest_file_not_directory():
    with tempfile.NamedTemporaryFile() as tmpfile:
        with pytest.raises(ValueError, match="Provided path is not a directory"):
            find_largest_file(tmpfile.name)

def test_find_largest_file_multiple_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple files with different sizes
        files = [
            ('file1.txt', 'small'),
            ('file2.txt', 'medium' * 10),
            ('file3.txt', 'large' * 100)
        ]
        
        for filename, content in files:
            with open(os.path.join(tmpdir, filename), 'w') as f:
                f.write(content)
        
        # Find largest file
        result_path, result_size = find_largest_file(tmpdir)
        
        assert result_path == os.path.join(tmpdir, 'file3.txt')
        assert result_size == len('large' * 100)