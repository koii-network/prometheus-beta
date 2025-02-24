import os
import pytest
import tempfile

from src.file_writer import write_string_to_file

def test_write_string_to_file_basic():
    """Test basic functionality of writing a string to a file."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        test_content = "Hello, world!"
        write_string_to_file(temp_path, test_content)
        
        with open(temp_path, 'r') as file:
            assert file.read() == test_content
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_write_string_to_file_empty_string():
    """Test writing an empty string to a file."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        write_string_to_file(temp_path, "")
        
        with open(temp_path, 'r') as file:
            assert file.read() == ""
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_write_string_to_file_overwrite():
    """Test that writing to an existing file overwrites its content."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        # First write
        write_string_to_file(temp_path, "First content")
        
        # Overwrite
        write_string_to_file(temp_path, "New content")
        
        with open(temp_path, 'r') as file:
            assert file.read() == "New content"
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_write_string_to_file_invalid_file_path():
    """Test that an error is raised for invalid file paths."""
    with pytest.raises(TypeError):
        write_string_to_file(None, "Content")
    
    with pytest.raises(TypeError):
        write_string_to_file(123, "Content")

def test_write_string_to_file_invalid_content():
    """Test that an error is raised for invalid content types."""
    with tempfile.NamedTemporaryFile(mode='r', delete=False) as temp_file:
        temp_path = temp_file.name
    
    try:
        with pytest.raises(TypeError):
            write_string_to_file(temp_path, None)
        
        with pytest.raises(TypeError):
            write_string_to_file(temp_path, 123)
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def test_write_string_to_file_empty_path():
    """Test that an error is raised for empty file paths."""
    with pytest.raises(ValueError):
        write_string_to_file("", "Content")
    
    with pytest.raises(ValueError):
        write_string_to_file("   ", "Content")