import os
import pytest
import tempfile
from src.find_largest_file import find_largest_file

def test_find_largest_file_normal_case():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test files with different sizes
        with open(os.path.join(tmpdir, 'small.txt'), 'w') as f:
            f.write('small')
        
        with open(os.path.join(tmpdir, 'large.txt'), 'w') as f:
            f.write('large' * 100)
        
        largest_file, size = find_largest_file(tmpdir)
        assert os.path.basename(largest_file) == 'large.txt'
        assert size == 500

def test_find_largest_file_empty_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        largest_file, size = find_largest_file(tmpdir)
        assert largest_file is None
        assert size == 0

def test_find_largest_file_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        find_largest_file('/path/to/nonexistent/directory')

def test_find_largest_file_not_a_directory():
    with tempfile.NamedTemporaryFile() as tmpfile:
        with pytest.raises(NotADirectoryError):
            find_largest_file(tmpfile.name)

def test_find_largest_file_includes_all_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple files of different sizes
        file_sizes = [10, 50, 20, 100, 5]
        file_names = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']
        
        for name, size in zip(file_names, file_sizes):
            with open(os.path.join(tmpdir, name), 'w') as f:
                f.write('x' * size)
        
        largest_file, size = find_largest_file(tmpdir)
        assert os.path.basename(largest_file) == 'file4.txt'
        assert size == 100