import os
import pytest
import tempfile
import pathlib

from src.symlink_detector import is_symlink

def test_is_symlink_on_regular_file():
    with tempfile.NamedTemporaryFile(delete=True) as temp_file:
        assert is_symlink(temp_file.name) == False

def test_is_symlink_on_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        assert is_symlink(temp_dir) == False

def test_is_symlink_on_symbolic_link():
    with tempfile.TemporaryDirectory() as temp_dir:
        original_file = os.path.join(temp_dir, 'original.txt')
        symlink_path = os.path.join(temp_dir, 'symlink.txt')
        
        # Create an original file
        with open(original_file, 'w') as f:
            f.write('test content')
        
        # Create a symbolic link
        os.symlink(original_file, symlink_path)
        
        assert is_symlink(symlink_path) == True

def test_is_symlink_invalid_input():
    with pytest.raises(TypeError):
        is_symlink(123)
    
    with pytest.raises(TypeError):
        is_symlink(None)

def test_is_symlink_nonexistent_path():
    with pytest.raises(FileNotFoundError):
        is_symlink('/path/to/nonexistent/file')