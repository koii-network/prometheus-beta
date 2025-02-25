"""
Tests for the file_string_replacer module.
"""

import os
import pytest
from src.file_string_replacer import replace_string_in_file

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    temp_file_path = tmp_path / "test_file.txt"
    temp_file_path.write_text("Hello world! Hello universe!")
    return str(temp_file_path)

def test_basic_string_replacement(temp_file):
    """Test basic string replacement."""
    result = replace_string_in_file(temp_file, "Hello", "Hi")
    assert result is True
    
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "Hi world! Hi universe!"

def test_no_replacements(temp_file):
    """Test when no replacements are made."""
    result = replace_string_in_file(temp_file, "Goodbye", "Hello")
    assert result is False
    
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "Hello world! Hello universe!"

def test_replace_with_empty_string(temp_file):
    """Test replacing with an empty string."""
    result = replace_string_in_file(temp_file, "world!", "")
    assert result is True
    
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "Hello  Hello universe!"

def test_replace_entire_content(temp_file):
    """Test replacing the entire content of the file."""
    result = replace_string_in_file(temp_file, "Hello world! Hello universe!", "Replaced")
    assert result is True
    
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "Replaced"

def test_invalid_file_path():
    """Test invalid file path."""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("non_existent_file.txt", "old", "new")

def test_invalid_input_types(temp_file):
    """Test invalid input types."""
    with pytest.raises(ValueError):
        replace_string_in_file(None, "old", "new")
    
    with pytest.raises(ValueError):
        replace_string_in_file(temp_file, None, "new")

def test_numeric_replacement(temp_file):
    """Test replacing with numeric values."""
    result = replace_string_in_file(temp_file, "Hello", 42)
    assert result is True
    
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "42 world! 42 universe!"