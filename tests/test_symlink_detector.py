import os
import pytest
import tempfile
import pathlib

from src.symlink_detector import is_symbolic_link

def test_is_symbolic_link_true():
    """Test that the function returns True for a symbolic link."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a real file
        original_file = os.path.join(tmpdir, 'original.txt')
        with open(original_file, 'w') as f:
            f.write('test content')
        
        # Create a symbolic link
        symlink_path = os.path.join(tmpdir, 'symlink.txt')
        os.symlink(original_file, symlink_path)
        
        assert is_symbolic_link(symlink_path) is True

def test_is_symbolic_link_false_regular_file():
    """Test that the function returns False for a regular file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a regular file
        regular_file = os.path.join(tmpdir, 'regular.txt')
        with open(regular_file, 'w') as f:
            f.write('test content')
        
        assert is_symbolic_link(regular_file) is False

def test_is_symbolic_link_false_directory():
    """Test that the function returns False for a directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        assert is_symbolic_link(tmpdir) is False

def test_is_symbolic_link_invalid_input():
    """Test error handling for invalid inputs."""
    # Test non-string input
    with pytest.raises(TypeError):
        is_symbolic_link(123)
    
    # Test empty string
    with pytest.raises(ValueError):
        is_symbolic_link('')

def test_is_symbolic_link_nonexistent_path():
    """Test behavior with a non-existent path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_path = os.path.join(tmpdir, 'nonexistent.txt')
        assert is_symbolic_link(nonexistent_path) is False