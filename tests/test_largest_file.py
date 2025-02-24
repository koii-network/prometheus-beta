import os
import pytest
import tempfile
import pathlib

from src.largest_file import find_largest_file

def test_find_largest_file_normal_case():
    # Create a temporary directory with test files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files with different sizes
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'medium.txt'), 'w') as f:
            f.write('medium sized file')
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large file with more content')
        
        # Find largest file
        largest = find_largest_file(tmpdir)
        
        # Assert largest file is the one with most content
        assert os.path.basename(largest) == 'large.txt'

def test_find_largest_file_empty_directory():
    # Test empty directory returns None
    with tempfile.TemporaryDirectory() as tmpdir:
        result = find_largest_file(tmpdir)
        assert result is None

def test_find_largest_file_nonexistent_directory():
    # Test nonexistent directory raises ValueError
    with pytest.raises(ValueError):
        find_largest_file('/path/to/nonexistent/directory')

def test_find_largest_file_not_a_directory():
    # Create a temporary file and test it raises ValueError
    with tempfile.NamedTemporaryFile() as tmpfile:
        with pytest.raises(ValueError):
            find_largest_file(tmpfile.name)

def test_find_largest_file_mixed_types():
    # Create a temporary directory with files and subdirectories
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create files with different sizes
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large file with more content')
        
        # Create a subdirectory (should be ignored)
        os.mkdir(os.path.join(tmpdir, 'subdir'))
        
        # Find largest file
        largest = find_largest_file(tmpdir)
        
        # Assert largest file is the one with most content
        assert os.path.basename(largest) == 'large.txt'

def test_find_largest_file_absolute_path_returned():
    # Ensure absolute path is returned
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, 'test.txt'), 'w') as f:
            f.write('test content')
        
        largest = find_largest_file(tmpdir)
        assert os.path.isabs(largest)
        assert os.path.exists(largest)