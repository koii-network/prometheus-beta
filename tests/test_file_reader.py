"""
Tests for the file_reader module.

This test suite covers various scenarios for reading text files,
including normal usage, edge cases, and error handling.
"""

import os
import pytest
import tempfile

from src.file_reader import read_text_file

def test_read_existing_text_file():
    """Test reading an existing text file."""
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

def test_read_file_with_unicode():
    """Test reading a file with unicode characters."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界")
        temp_file.close()
        
        try:
            content = read_text_file(temp_file.name)
            assert content == "こんにちは世界"
        finally:
            os.unlink(temp_file.name)

def test_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        read_text_file("non_existent_file.txt")

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    # Test with None
    with pytest.raises(ValueError):
        read_text_file(None)
    
    # Test with empty string
    with pytest.raises(ValueError):
        read_text_file("")
    
    # Test with non-string input
    with pytest.raises(ValueError):
        read_text_file(123)

def test_directory_path():
    """Test that IsADirectoryError is raised when path is a directory."""
    with pytest.raises(IsADirectoryError):
        read_text_file(".")