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
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_append(tmp_path):
    """Test appending to an existing file."""
    test_file = tmp_path / "append_test.txt"
    
    # First write
    write_string_to_file(str(test_file), "First line\n")
    
    # Append 
    write_string_to_file(str(test_file), "Second line\n", mode='a')
    
    with open(test_file, 'r', encoding='utf-8') as file:
        content = file.read()
        assert content == "First line\n" + "Second line\n"

def test_write_string_to_file_invalid_path_type():
    """Test that TypeError is raised for non-string path."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "test content")

def test_write_string_to_file_invalid_content_type():
    """Test that TypeError is raised for non-string content."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_empty_path():
    """Test that ValueError is raised for empty path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "test content")

def test_write_string_to_file_empty_content(tmp_path):
    """Test writing an empty string to a file."""
    test_file = tmp_path / "empty_file.txt"
    
    write_string_to_file(str(test_file), "")
    
    assert test_file.exists()
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == ""