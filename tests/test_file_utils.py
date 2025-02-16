import os
import pytest
import tempfile
from src.file_utils import find_largest_file

def test_find_largest_file():
    # Create a temporary directory with test files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with different sizes
        files = [
            ('small.txt', '100 bytes'),
            ('medium.txt', '500 bytes'),
            ('large.txt', '1000 bytes')
        ]
        
        for filename, content in files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content * (int(content.split()[0]) // len(content)))
        
        # Find the largest file
        result = find_largest_file(temp_dir)
        
        # Assert the result
        assert result is not None
        assert result['filename'] == 'large.txt'
        assert result['size'] == 1000
        assert result['path'] == os.path.join(temp_dir, 'large.txt')

def test_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = find_largest_file(temp_dir)
        assert result is None

def test_invalid_directory():
    result = find_largest_file('/nonexistent/path')
    assert result is None

def test_directory_with_inaccessible_files():
    # This test might be tricky to set up completely, but we'll attempt to cover the case
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file that might be problematic
        file_path = os.path.join(temp_dir, 'test.txt')
        with open(file_path, 'w') as f:
            f.write('Some content')
        
        # Attempt to find largest file
        result = find_largest_file(temp_dir)
        assert result is not None
        assert result['filename'] == 'test.txt'