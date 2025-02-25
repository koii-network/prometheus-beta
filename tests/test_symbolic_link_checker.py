import os
import pytest
import tempfile
import pathlib

from src.symbolic_link_checker import is_symbolic_link

def test_is_symbolic_link_on_regular_file():
    """Test that a regular file returns False."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert is_symbolic_link(temp_file_path) == False
    finally:
        os.unlink(temp_file_path)

def test_is_symbolic_link_on_symlink():
    """Test that a symbolic link returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a real file
        original_file = os.path.join(temp_dir, 'original.txt')
        with open(original_file, 'w') as f:
            f.write('test content')
        
        # Create a symbolic link
        symlink_path = os.path.join(temp_dir, 'symlink.txt')
        os.symlink(original_file, symlink_path)
        
        assert is_symbolic_link(symlink_path) == True

def test_is_symbolic_link_with_non_existent_file():
    """Test that a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        is_symbolic_link('/path/to/non/existent/file.txt')

def test_is_symbolic_link_with_invalid_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_symbolic_link(123)
    
    with pytest.raises(TypeError):
        is_symbolic_link(None)