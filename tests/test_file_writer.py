"""
Tests for the file_writer module.
"""

import os
import pytest
import tempfile

from src.file_writer import write_string_to_file

def test_write_string_to_file_basic():
    """Test basic functionality of writing a string to a file."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    test_content = "Hello, world!"
    write_string_to_file(temp_path, test_content)
    
    with open(temp_path, 'r') as file:
        assert file.read() == test_content
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_overwrite():
    """Test that writing to an existing file overwrites its content."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    # First write
    write_string_to_file(temp_path, "First content")
    
    # Overwrite
    test_content = "Overwritten content"
    write_string_to_file(temp_path, test_content)
    
    with open(temp_path, 'r') as file:
        assert file.read() == test_content
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_empty_string():
    """Test writing an empty string to a file."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    write_string_to_file(temp_path, "")
    
    with open(temp_path, 'r') as file:
        assert file.read() == ""
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_unicode():
    """Test writing a file with unicode characters."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    test_content = "Hello, 世界! こんにちは"
    write_string_to_file(temp_path, test_content)
    
    with open(temp_path, 'r', encoding='utf-8') as file:
        assert file.read() == test_content
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_invalid_filepath():
    """Test that an invalid filepath raises an appropriate error."""
    with pytest.raises(TypeError):
        write_string_to_file(None, "Test")
    
    with pytest.raises(ValueError):
        write_string_to_file("", "Test")

def test_write_string_to_file_invalid_content():
    """Test that invalid content type raises a TypeError."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    with pytest.raises(TypeError):
        write_string_to_file(temp_path, None)
    
    with pytest.raises(TypeError):
        write_string_to_file(temp_path, 12345)
    
    # Clean up
    os.unlink(temp_path)