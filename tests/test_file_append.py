import os
import pytest

from src.file_append import append_to_file

def test_append_to_existing_file(tmp_path):
    """Test appending text to an existing file."""
    # Create a temporary file
    test_file = tmp_path / "test_append.txt"
    test_file.write_text("Initial content\n")
    
    # Append text
    append_to_file(str(test_file), "Additional text\n")
    
    # Check content
    assert test_file.read_text() == "Initial content\nAdditional text\n"

def test_append_to_empty_file(tmp_path):
    """Test appending text to an empty file."""
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()  # Create an empty file
    
    append_to_file(str(test_file), "Some content\n")
    
    assert test_file.read_text() == "Some content\n"

def test_invalid_file_path():
    """Test that a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        append_to_file("nonexistent/path/file.txt", "Some text")

def test_invalid_input_types():
    """Test input type validation."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        append_to_file(123, "text")
    
    with pytest.raises(TypeError, match="text must be a string"):
        append_to_file("test.txt", 456)

def test_appending_empty_string(tmp_path):
    """Test appending an empty string."""
    test_file = tmp_path / "empty_append.txt"
    test_file.write_text("Initial content\n")
    
    append_to_file(str(test_file), "")
    
    assert test_file.read_text() == "Initial content\n"