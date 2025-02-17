import os
import pytest
import tempfile
from src.file_utils import find_largest_file

def test_find_largest_file_basic():
    """Test finding the largest file in a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files with different sizes
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        # Find the largest file
        largest = find_largest_file(tmpdir)
        assert largest.endswith('large.txt')

def test_find_largest_file_empty_directory():
    """Test behavior with an empty directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        assert find_largest_file(tmpdir) is None

def test_find_largest_file_nonexistent_directory():
    """Test raising FileNotFoundError for nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        find_largest_file('/path/that/does/not/exist')

def test_find_largest_file_not_a_directory():
    """Test raising NotADirectoryError when path is not a directory."""
    with tempfile.NamedTemporaryFile() as tmpfile:
        with pytest.raises(NotADirectoryError):
            find_largest_file(tmpfile.name)

def test_find_largest_file_with_subdirectories():
    """Test finding largest file while ignoring subdirectories."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files and a subdirectory
        with open(os.path.join(tmpdir, 'file1.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'file2.txt'), 'w') as f:
            f.write('large' * 100)
        
        # Create a subdirectory with a file
        subdir = os.path.join(tmpdir, 'subdir')
        os.makedirs(subdir)
        with open(os.path.join(subdir, 'subfile.txt'), 'w') as f:
            f.write('medium' * 50)
        
        # Find the largest file
        largest = find_largest_file(tmpdir)
        assert largest.endswith('file2.txt')