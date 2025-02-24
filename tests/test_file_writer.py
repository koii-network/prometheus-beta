"""
Tests for the file_writer module.
"""

import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_basic(tmp_path):
    """Test basic file writing functionality."""
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    
    write_string_to_file(str(test_file), test_content)
    
    assert test_file.exists()
    assert test_file.read_text() == test_content

def test_write_string_to_file_overwrite(tmp_path):
    """Test overwriting an existing file."""
    test_file = tmp_path / "test_file.txt"
    
    # Write initial content
    write_string_to_file(str(test_file), "Initial content")
    
    # Overwrite with new content
    new_content = "New content"
    write_string_to_file(str(test_file), new_content)
    
    assert test_file.read_text() == new_content

def test_write_string_to_file_empty_string(tmp_path):
    """Test writing an empty string."""
    test_file = tmp_path / "test_file.txt"
    
    write_string_to_file(str(test_file), "")
    
    assert test_file.exists()
    assert test_file.read_text() == ""

def test_write_string_to_file_unicode(tmp_path):
    """Test writing unicode characters."""
    test_file = tmp_path / "test_file.txt"
    test_content = "こんにちは世界"
    
    write_string_to_file(str(test_file), test_content)
    
    assert test_file.read_text() == test_content

def test_write_string_to_file_invalid_file_path_type():
    """Test raising TypeError for invalid file path type."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    """Test raising TypeError for invalid content type."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("file.txt", 123)

def test_write_string_to_file_empty_file_path():
    """Test raising ValueError for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")

def test_write_string_to_file_invalid_directory(tmp_path):
    """Test handling of invalid directory."""
    with pytest.raises(IOError):
        write_string_to_file(str(tmp_path / "non_existent_dir" / "file.txt"), "content")