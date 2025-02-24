import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_text_file_success():
    """Test reading a text file successfully."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_text_file_empty():
    """Test reading an empty text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_read_text_file_non_existent():
    """Test reading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("non_existent_file.txt")

def test_read_text_file_unicode():
    """Test reading a text file with unicode characters."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "こんにちは世界"
        finally:
            os.unlink(temp_file.name)