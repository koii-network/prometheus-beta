import os
import pytest
import tempfile
import pathlib

from src.symlink_detector import is_symlink

def test_is_symlink_with_real_symlink():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create an original file
        original_file = os.path.join(tmpdir, 'original.txt')
        with open(original_file, 'w') as f:
            f.write('Test content')
        
        # Create a symbolic link
        symlink_path = os.path.join(tmpdir, 'symlink.txt')
        os.symlink(original_file, symlink_path)
        
        # Test the function
        assert is_symlink(symlink_path) is True

def test_is_symlink_with_regular_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a regular file
        regular_file = os.path.join(tmpdir, 'regular.txt')
        with open(regular_file, 'w') as f:
            f.write('Test content')
        
        # Test the function
        assert is_symlink(regular_file) is False

def test_is_symlink_with_nonexistent_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_path = os.path.join(tmpdir, 'nonexistent.txt')
        
        # Test that FileNotFoundError is raised
        with pytest.raises(FileNotFoundError):
            is_symlink(nonexistent_path)

def test_is_symlink_with_invalid_input():
    # Test that TypeError is raised for non-string inputs
    with pytest.raises(TypeError):
        is_symlink(123)
    
    with pytest.raises(TypeError):
        is_symlink(None)

def test_is_symlink_with_directory_symlink():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create an original directory
        original_dir = os.path.join(tmpdir, 'original_dir')
        os.makedirs(original_dir)
        
        # Create a directory symlink
        dir_symlink = os.path.join(tmpdir, 'dir_symlink')
        os.symlink(original_dir, dir_symlink)
        
        # Test the function
        assert is_symlink(dir_symlink) is True