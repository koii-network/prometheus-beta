import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_existing_text_file():
    """Test reading an existing text file with content."""
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

def test_read_non_existent_file():
    """Test reading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_text_file("/path/to/non/existent/file.txt")

def test_read_directory():
    """Test reading a directory raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        read_text_file(tempfile.gettempdir())

def test_file_with_special_characters():
    """Test reading a file with special characters and UTF-8 encoding."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界！ Hello, 世界!")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "こんにちは世界！ Hello, 世界!"
        finally:
            os.unlink(temp_file.name)

def test_large_file():
    """Test reading a relatively large text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        large_content = "Test content\n" * 1000
        temp_file.write(large_content)
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == large_content
        finally:
            os.unlink(temp_file.name)