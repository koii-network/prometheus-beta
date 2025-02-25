import os
import pytest
import tempfile
import pathlib

from src.file_hidden_check import is_hidden_file

def test_hidden_file_unix_style():
    """Test detecting Unix-style hidden files (starting with .)"""
    with tempfile.TemporaryDirectory() as tmpdir:
        hidden_file = os.path.join(tmpdir, '.hidden_file.txt')
        visible_file = os.path.join(tmpdir, 'visible_file.txt')
        
        pathlib.Path(hidden_file).touch()
        pathlib.Path(visible_file).touch()
        
        assert is_hidden_file(hidden_file) == True
        assert is_hidden_file(visible_file) == False

def test_invalid_input_types():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        is_hidden_file(None)
    with pytest.raises(TypeError):
        is_hidden_file(123)
    with pytest.raises(TypeError):
        is_hidden_file(['file'])

def test_nonexistent_file():
    """Test that non-existent files raise FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        is_hidden_file('/path/to/nonexistent/file.txt')

def test_file_with_dot_in_middle():
    """Test file with dot in middle is not considered hidden"""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'not.hidden.txt')
        pathlib.Path(file_path).touch()
        
        assert is_hidden_file(file_path) == False

def test_hidden_file_with_path_variants():
    """Test hidden file detection with different path representations"""
    with tempfile.TemporaryDirectory() as tmpdir:
        hidden_file = os.path.join(tmpdir, '.test_file.txt')
        pathlib.Path(hidden_file).touch()
        
        # Test relative paths, absolute paths, and with user expansion
        test_paths = [
            hidden_file,  # absolute path
            os.path.relpath(hidden_file),  # relative path
            '.test_file.txt'  # filename in current dir
        ]
        
        for path in test_paths:
            assert is_hidden_file(path) == True