import os
import pytest
import tempfile
from src.file_reader import read_file_contents

def test_read_file_contents_success():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        test_content = "Hello, this is a test file!"
        temp_file.write(test_content)
        temp_file.close()
    
    try:
        # Read the file and verify contents
        result = read_file_contents(temp_file.name)
        assert result == test_content
    finally:
        # Clean up the temporary file
        os.unlink(temp_file.name)

def test_read_file_contents_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
    
    try:
        # Read the empty file
        result = read_file_contents(temp_file.name)
        assert result == ""
    finally:
        # Clean up the temporary file
        os.unlink(temp_file.name)

def test_read_file_contents_nonexistent_file():
    # Test reading a non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_contents('non_existent_file.txt')

def test_read_file_contents_unicode():
    # Create a temporary file with Unicode content
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        unicode_content = "こんにちは World! 🌍"
        temp_file.write(unicode_content)
        temp_file.close()
    
    try:
        # Read the file and verify Unicode contents
        result = read_file_contents(temp_file.name)
        assert result == unicode_content
    finally:
        # Clean up the temporary file
        os.unlink(temp_file.name)