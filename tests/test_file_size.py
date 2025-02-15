import os
import pytest
from src.file_size import get_file_size

def test_get_file_size():
    # Create a temporary test file
    test_file = 'tests/test_file.txt'
    with open(test_file, 'w') as f:
        f.write('Hello, World!')
    
    try:
        # Check if file size is correct
        assert get_file_size(test_file) == 13  # 13 bytes for "Hello, World!"
    finally:
        # Clean up the test file
        os.remove(test_file)

def test_non_existent_file():
    with pytest.raises(FileNotFoundError):
        get_file_size('non_existent_file.txt')

def test_directory_size():
    with pytest.raises(IsADirectoryError):
        get_file_size('tests')

def test_zero_byte_file():
    # Create a zero-byte file
    test_file = 'tests/zero_byte_file.txt'
    open(test_file, 'w').close()
    
    try:
        assert get_file_size(test_file) == 0
    finally:
        os.remove(test_file)