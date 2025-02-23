import os
import pytest
import tempfile
from src.file_writer import write_string_to_file

def test_write_string_to_file_success():
    """Test writing a string to a file successfully."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    test_content = "Hello, world!"
    write_string_to_file(temp_path, test_content)
    
    # Verify file contents
    with open(temp_path, 'r', encoding='utf-8') as file:
        assert file.read() == test_content
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_overwrite():
    """Test that writing to an existing file overwrites its contents."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Original content")
        temp_file.flush()
        temp_path = temp_file.name
    
    new_content = "New content"
    write_string_to_file(temp_path, new_content)
    
    # Verify file contents
    with open(temp_path, 'r', encoding='utf-8') as file:
        assert file.read() == new_content
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_invalid_file_path_type():
    """Test raising TypeError for non-string file path."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    """Test raising TypeError for non-string content."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name
    
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file(temp_path, 123)
    
    # Clean up
    os.unlink(temp_path)

def test_write_string_to_file_empty_file_path():
    """Test raising ValueError for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")