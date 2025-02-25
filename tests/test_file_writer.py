"""
Test suite for the file_writer module.
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
    
    # First write
    write_string_to_file(str(test_file), "Initial content")
    
    # Overwrite
    write_string_to_file(str(test_file), "New content", overwrite=True)
    
    assert test_file.read_text() == "New content"


def test_write_string_to_file_no_overwrite(tmp_path):
    """Test preventing overwrite of existing file."""
    test_file = tmp_path / "test_file.txt"
    
    # First write
    write_string_to_file(str(test_file), "Initial content")
    
    # Try to write again without overwrite
    with pytest.raises(IOError, match="already exists"):
        write_string_to_file(str(test_file), "New content")


def test_write_string_to_file_invalid_content():
    """Test handling of invalid content types."""
    with pytest.raises(ValueError, match="Content must be a string"):
        write_string_to_file("test.txt", 123)
    
    with pytest.raises(ValueError, match="Content must be a string"):
        write_string_to_file("test.txt", None)


def test_write_string_to_file_invalid_path():
    """Test handling of invalid file paths."""
    with pytest.raises(ValueError, match="File path must be a non-empty string"):
        write_string_to_file("", "content")
    
    with pytest.raises(ValueError, match="File path must be a non-empty string"):
        write_string_to_file(None, "content")


def test_write_string_to_file_encoding(tmp_path):
    """Test writing with different encodings."""
    test_file = tmp_path / "test_file.txt"
    test_content = "こんにちは"  # Japanese "Hello"
    
    write_string_to_file(str(test_file), test_content, encoding='utf-8')
    
    assert test_file.read_text(encoding='utf-8') == test_content