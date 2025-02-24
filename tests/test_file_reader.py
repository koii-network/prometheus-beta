import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_existing_text_file():
    """Test reading the contents of an existing text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_read_non_existing_file():
    """Test reading a non-existing file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("/path/to/non/existing/file.txt")

def test_read_file_with_special_characters():
    """Test reading a file with special characters and UTF-8 encoding."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界\nMultiline text with special chars: !@#$%^&*()")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "こんにちは世界\nMultiline text with special chars: !@#$%^&*()"
        finally:
            os.unlink(temp_file.name)