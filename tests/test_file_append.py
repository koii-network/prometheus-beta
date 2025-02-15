import os
import pytest
from src.file_append import append_text_to_file

def test_append_text_to_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Initial content\n")
    
    # Append text
    append_text_to_file(str(test_file), "Additional text\n")
    
    # Check file contents
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "Initial content\n" + "Additional text\n"

def test_append_empty_string(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "empty_test.txt"
    test_file.write_text("Initial content\n")
    
    # Append empty string
    append_text_to_file(str(test_file), "")
    
    # Check file contents remain unchanged
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "Initial content\n"

def test_file_not_found():
    # Try to append to a non-existent file
    with pytest.raises(FileNotFoundError):
        append_text_to_file("non_existent_file.txt", "Some text")

def test_invalid_file_path_type():
    # Try to pass a non-string file path
    with pytest.raises(TypeError):
        append_text_to_file(123, "Some text")

def test_invalid_text_type():
    # Try to pass a non-string text to append
    with pytest.raises(TypeError):
        append_text_to_file("some_file.txt", 456)