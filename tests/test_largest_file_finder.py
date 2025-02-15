import os
import pytest
import tempfile
import shutil

from src.largest_file_finder import find_largest_file

def test_find_largest_file_empty_directory():
    """Test that an empty directory returns (None, 0)"""
    with tempfile.TemporaryDirectory() as temp_dir:
        result = find_largest_file(temp_dir)
        assert result == (None, 0)

def test_find_largest_file_single_file():
    """Test finding the largest file when there's only one file"""
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('Hello World')
        
        result = find_largest_file(temp_dir)
        assert result == (test_file, 11)

def test_find_largest_file_multiple_files():
    """Test finding the largest file among multiple files"""
    with tempfile.TemporaryDirectory() as temp_dir:
        files = [
            os.path.join(temp_dir, 'small.txt'),
            os.path.join(temp_dir, 'medium.txt'),
            os.path.join(temp_dir, 'large.txt')
        ]
        
        # Create files with different sizes
        with open(files[0], 'w') as f:
            f.write('small')
        with open(files[1], 'w') as f:
            f.write('medium sized file')
        with open(files[2], 'w') as f:
            f.write('large file with more content')
        
        result = find_largest_file(temp_dir)
        assert result == (files[2], 27)

def test_find_largest_file_nested_directories():
    """Test finding the largest file in nested directories"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory structure
        os.makedirs(os.path.join(temp_dir, 'subdir1'))
        os.makedirs(os.path.join(temp_dir, 'subdir2'))
        
        files = [
            os.path.join(temp_dir, 'small.txt'),
            os.path.join(temp_dir, 'subdir1', 'medium.txt'),
            os.path.join(temp_dir, 'subdir2', 'large.txt')
        ]
        
        # Create files with different sizes
        with open(files[0], 'w') as f:
            f.write('small')
        with open(files[1], 'w') as f:
            f.write('medium sized file')
        with open(files[2], 'w') as f:
            f.write('large file with more content')
        
        result = find_largest_file(temp_dir)
        assert result == (files[2], 27)

def test_find_largest_file_invalid_directory():
    """Test that an invalid directory raises NotADirectoryError"""
    with pytest.raises(NotADirectoryError):
        find_largest_file('/path/that/does/not/exist')

def test_find_largest_file_current_directory_default():
    """Test that the function works with default current directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        original_cwd = os.getcwd()
        try:
            os.chdir(temp_dir)
            
            # Create a file in the current directory
            with open('test.txt', 'w') as f:
                f.write('Test content')
            
            result = find_largest_file()
            assert result == ('test.txt', 12)
        finally:
            os.chdir(original_cwd)