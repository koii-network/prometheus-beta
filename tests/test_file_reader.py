"""
Tests for the file_reader module.
"""

import os
import pytest
import tempfile

from src.file_reader import read_file_contents

def test_read_valid_file():
    """Test reading a valid text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_file_not_found():
    """Test reading a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_file_contents("/path/to/nonexistent/file.txt")

def test_is_directory():
    """Test attempting to read a directory raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        read_file_contents(os.path.dirname(os.path.abspath(__file__)))

def test_unicode_file():
    """Test reading a file with unicode content."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界")
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == "こんにちは世界"
        finally:
            os.unlink(temp_file.name)

def test_large_file():
    """Test reading a large file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        large_content = "x" * 1_000_000  # 1 million characters
        temp_file.write(large_content)
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == large_content
        finally:
            os.unlink(temp_file.name)