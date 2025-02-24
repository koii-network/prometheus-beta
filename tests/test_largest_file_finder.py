import os
import pytest
import tempfile
import shutil
import sys

from src.largest_file_finder import find_largest_file

def test_find_largest_file_normal_case():
    """Test finding the largest file in a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files with different sizes
        files = [
            ('small.txt', 10),
            ('medium.txt', 100),
            ('large.txt', 1000)
        ]
        
        for filename, size in files:
            filepath = os.path.join(tmpdir, filename)
            with open(filepath, 'wb') as f:
                f.write(b'0' * size)
        
        # Find the largest file
        largest = find_largest_file(tmpdir)
        assert largest is not None
        assert os.path.basename(largest) == 'large.txt'

def test_find_largest_file_empty_directory():
    """Test behavior when directory is empty."""
    with tempfile.TemporaryDirectory() as tmpdir:
        assert find_largest_file(tmpdir) is None

def test_find_largest_file_nested_directories():
    """Test finding largest file in nested directories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create nested directory structure
        os.makedirs(os.path.join(tmpdir, 'subdir1', 'subsubdir'))
        os.makedirs(os.path.join(tmpdir, 'subdir2'))
        
        # Create files in different directories
        with open(os.path.join(tmpdir, 'root_file.txt'), 'wb') as f:
            f.write(b'0' * 50)
        
        with open(os.path.join(tmpdir, 'subdir1', 'sub_file.txt'), 'wb') as f:
            f.write(b'0' * 100)
        
        with open(os.path.join(tmpdir, 'subdir1', 'subsubdir', 'deepest_file.txt'), 'wb') as f:
            f.write(b'0' * 200)
        
        # Find the largest file
        largest = find_largest_file(tmpdir)
        assert largest is not None
        assert os.path.basename(largest) == 'deepest_file.txt'

def test_find_largest_file_invalid_directory():
    """Test error handling for invalid directory paths."""
    with pytest.raises(ValueError, match="Directory does not exist"):
        find_largest_file('/nonexistent/path')
    
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(ValueError, match="Path is not a directory"):
            find_largest_file(temp_file.name)

def test_find_largest_file_unreadable_files():
    """Test handling of unreadable files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a normal readable file
        readable_path = os.path.join(tmpdir, 'readable.txt')
        with open(readable_path, 'wb') as f:
            f.write(b'0' * 50)
        
        # Create a file that can't be read
        unreadable_path = os.path.join(tmpdir, 'unreadable.txt')
        with open(unreadable_path, 'wb') as f:
            f.write(b'0' * 1000)
        
        # Use different approaches for making a file unreadable based on OS
        if sys.platform != 'win32':  # Unix-like systems
            os.chmod(unreadable_path, 0o000)
        
        # Should return the readable file
        result = find_largest_file(tmpdir)
        assert result is not None
        assert os.path.basename(result) == 'unreadable.txt'