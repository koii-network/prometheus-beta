import os
import pytest
import tempfile
from src.file_reader import read_text_file

def test_read_text_file_successful():
    """Test successful reading of a text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        test_content = "Hello, world!\nThis is a test file."
        temp_file.write(test_content)
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == test_content
        finally:
            os.unlink(temp_file.name)

def test_read_text_file_empty():
    """Test reading an empty text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("")
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == ""
        finally:
            os.unlink(temp_file.name)

def test_read_text_file_nonexistent():
    """Test reading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("nonexistent_file.txt")

def test_read_text_file_utf8_encoding():
    """Test reading a file with UTF-8 characters."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        test_content = "こんにちは世界\nÑáéíóú"
        temp_file.write(test_content)
        temp_file.close()
        
        try:
            result = read_text_file(temp_file.name)
            assert result == test_content
        finally:
            os.unlink(temp_file.name)