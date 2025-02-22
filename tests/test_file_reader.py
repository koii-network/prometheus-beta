import os
import pytest
from src.file_reader import read_text_file

def test_read_text_file_successful():
    # Create a temporary test file
    test_file_path = 'tests/test_data.txt'
    test_content = 'Hello, world!\nThis is a test file.'
    
    try:
        with open(test_file_path, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        # Test reading the file
        result = read_text_file(test_file_path)
        assert result == test_content
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_text_file('nonexistent_file.txt')

def test_read_empty_file():
    # Create an empty file
    test_file_path = 'tests/empty_test_file.txt'
    
    try:
        with open(test_file_path, 'w', encoding='utf-8') as f:
            pass  # Create an empty file
        
        result = read_text_file(test_file_path)
        assert result == ''
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_read_file_with_unicode():
    # Create a file with Unicode content
    test_file_path = 'tests/unicode_test_file.txt'
    test_content = 'Hello, 世界! こんにちは'
    
    try:
        with open(test_file_path, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        result = read_text_file(test_file_path)
        assert result == test_content
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)