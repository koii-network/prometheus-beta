import os
import pytest
import tempfile
from src.file_readonly_check import is_file_readonly

def test_is_file_readonly():
    # Test with a writable file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_writable:
        temp_writable_path = temp_writable.name
        try:
            assert is_file_readonly(temp_writable_path) == False
        finally:
            os.unlink(temp_writable_path)

    # Test with a read-only file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file_path = temp_file.name
        try:
            # Make the file read-only
            os.chmod(temp_file_path, 0o444)
            assert is_file_readonly(temp_file_path) == True
        finally:
            os.unlink(temp_file_path)

def test_is_file_readonly_nonexistent_file():
    # Test with a non-existent file
    with pytest.raises(FileNotFoundError):
        is_file_readonly('/path/to/nonexistent/file.txt')

def test_gitignore_readonly():
    # Test the .gitignore file
    assert is_file_readonly('.gitignore') == False