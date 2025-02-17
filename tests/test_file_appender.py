import os
import pytest
from src.file_appender import append_text_to_file

def test_append_text_to_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_append.txt"
    test_file.write_text("Initial content\n")
    
    # Append text
    append_text_to_file(str(test_file), "Additional text\n")
    
    # Check the content
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "Initial content\nAdditional text\n"

def test_append_text_to_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Append text
    append_text_to_file(str(test_file), "First text\n")
    
    # Check the content
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "First text\n"

def test_raise_file_not_found():
    # Attempt to append to a non-existent file
    with pytest.raises(FileNotFoundError):
        append_text_to_file("non_existent_file.txt", "Some text")

def test_raise_type_error_invalid_file_path():
    # Attempt to append with invalid file path type
    with pytest.raises(TypeError, match="file_path must be a string"):
        append_text_to_file(123, "Some text")

def test_raise_type_error_invalid_text():
    # Attempt to append with invalid text type
    with pytest.raises(TypeError, match="text_to_append must be a string"):
        append_text_to_file("test.txt", 456)