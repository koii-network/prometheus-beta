import os
import pytest
from src.file_append import append_text_to_file

def test_append_text_to_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Initial content\n")
    
    # Append text to the file
    result = append_text_to_file(str(test_file), "Additional text\n")
    
    # Verify the append was successful
    assert result is True
    assert test_file.read_text() == "Initial content\nAdditional text\n"

def test_append_multiple_times(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "multi_append.txt"
    test_file.write_text("First line\n")
    
    # Append multiple times
    append_text_to_file(str(test_file), "Second line\n")
    append_text_to_file(str(test_file), "Third line\n")
    
    # Verify the content
    assert test_file.read_text() == "First line\nSecond line\nThird line\n"

def test_file_not_found(tmp_path):
    # Try to append to a non-existent file
    with pytest.raises(FileNotFoundError):
        append_text_to_file(str(tmp_path / "non_existent.txt"), "Some text")

def test_empty_text(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "empty_append.txt"
    test_file.write_text("Initial content\n")
    
    # Append empty text
    result = append_text_to_file(str(test_file), "")
    
    # Verify no change
    assert result is True
    assert test_file.read_text() == "Initial content\n"