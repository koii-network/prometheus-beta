import os
import pytest
import tempfile
import shutil

from src.file_hidden import is_hidden_file

def test_hidden_file_with_dot_prefix():
    with tempfile.TemporaryDirectory() as tmpdir:
        hidden_file_path = os.path.join(tmpdir, '.hidden_file.txt')
        with open(hidden_file_path, 'w') as f:
            f.write('test')
        assert is_hidden_file(hidden_file_path) == True

def test_non_hidden_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        visible_file_path = os.path.join(tmpdir, 'visible_file.txt')
        with open(visible_file_path, 'w') as f:
            f.write('test')
        assert is_hidden_file(visible_file_path) == False

def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        is_hidden_file('/path/to/nonexistent/file.txt')

def test_invalid_path_type():
    with pytest.raises(TypeError):
        is_hidden_file(123)

def test_empty_string_path():
    with pytest.raises(FileNotFoundError):
        is_hidden_file('')

def test_user_path_expansion():
    # Create a hidden file in user's home directory
    hidden_file_path = os.path.expanduser('~/.test_hidden_file.txt')
    try:
        with open(hidden_file_path, 'w') as f:
            f.write('test')
        assert is_hidden_file('~/.test_hidden_file.txt') == True
    finally:
        # Clean up the test file
        if os.path.exists(hidden_file_path):
            os.remove(hidden_file_path)