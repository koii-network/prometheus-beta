import os
import pytest
import tempfile
import sys
import platform

# Import the function from the source file
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.is_hidden_file import is_hidden_file

def test_hidden_file_unix_style():
    # Create a hidden file
    with tempfile.TemporaryDirectory() as tmpdir:
        hidden_file_path = os.path.join(tmpdir, '.hidden_file.txt')
        with open(hidden_file_path, 'w') as f:
            f.write('test')
        
        assert is_hidden_file(hidden_file_path) == True

def test_non_hidden_file():
    # Create a non-hidden file
    with tempfile.TemporaryDirectory() as tmpdir:
        visible_file_path = os.path.join(tmpdir, 'visible_file.txt')
        with open(visible_file_path, 'w') as f:
            f.write('test')
        
        assert is_hidden_file(visible_file_path) == False

def test_invalid_file_path():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        is_hidden_file('/path/to/non/existent/file.txt')

def test_invalid_input_type():
    # Test invalid input type
    with pytest.raises(TypeError):
        is_hidden_file(123)  # Not a string

def test_relative_path():
    # Create a hidden file and test with relative path
    with tempfile.TemporaryDirectory() as tmpdir:
        # Change current working directory
        original_cwd = os.getcwd()
        os.chdir(tmpdir)
        
        try:
            hidden_file_path = '.hidden_relative.txt'
            with open(hidden_file_path, 'w') as f:
                f.write('test')
            
            assert is_hidden_file(hidden_file_path) == True
        finally:
            # Restore original working directory
            os.chdir(original_cwd)