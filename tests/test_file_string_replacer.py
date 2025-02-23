"""
Tests for the file string replacement function.
"""

import os
import pytest
from src.file_string_replacer import replace_string_in_file

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world! Hello universe! Hello galaxy!")
    return str(test_file)

def test_replace_string_basic(temp_file):
    """Test basic string replacement."""
    replacements = replace_string_in_file(temp_file, "Hello", "Hi")
    
    assert replacements == 3
    with open(temp_file, 'r') as file:
        content = file.read()
        assert content == "Hi world! Hi universe! Hi galaxy!"

def test_replace_no_occurrences(temp_file):
    """Test when no replacements are made."""
    replacements = replace_string_in_file(temp_file, "Goodbye", "Hi")
    
    assert replacements == 0
    with open(temp_file, 'r') as file:
        content = file.read()
        assert content == "Hello world! Hello universe! Hello galaxy!"

def test_replace_with_empty_new_string(temp_file):
    """Test replacing with an empty string."""
    replacements = replace_string_in_file(temp_file, "Hello ", "")
    
    assert replacements == 3
    with open(temp_file, 'r') as file:
        content = file.read()
        assert content.startswith("world!")
        assert "Hello" not in content

def test_file_not_found():
    """Test when the file does not exist."""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("nonexistent_file.txt", "old", "new")

def test_invalid_input_types():
    """Test input type validation."""
    with pytest.raises(TypeError):
        replace_string_in_file(123, "old", "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", 123, "new")
    
    with pytest.raises(TypeError):
        replace_string_in_file("file.txt", "old", 123)

def test_empty_old_string(temp_file):
    """Test raising ValueError for empty old string."""
    with pytest.raises(ValueError):
        replace_string_in_file(temp_file, "", "new")