import os
import pytest
import tempfile
import pathlib

from src.symlink_detector import is_symbolic_link

def test_is_symbolic_link():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a regular file
        regular_file = os.path.join(tmpdir, 'regular_file.txt')
        with open(regular_file, 'w') as f:
            f.write('Test content')
        
        # Create a symbolic link
        symlink_path = os.path.join(tmpdir, 'symlink')
        os.symlink(regular_file, symlink_path)
        
        # Test cases
        assert is_symbolic_link(symlink_path) == True
        assert is_symbolic_link(regular_file) == False

def test_is_symbolic_link_error_handling():
    # Test non-string input
    with pytest.raises(TypeError):
        is_symbolic_link(123)
    
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        is_symbolic_link('/path/to/nonexistent/file')