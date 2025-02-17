import os
import pytest
from src.file_append import append_text_to_file

def test_append_text_to_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_append.txt"
    test_file.write_text("Initial content\n")
    
    # Append text
    append_text_to_file(str(test_file), "Additional text\n")
    
    # Verify content
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "Initial content\n" + "Additional text\n"

def test_append_to_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Append text
    append_text_to_file(str(test_file), "First content\n")
    
    # Verify content
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "First content\n"

def test_append_multiple_times(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "multiple_append.txt"
    test_file.write_text("Initial content\n")
    
    # Append multiple times
    append_text_to_file(str(test_file), "Second line\n")
    append_text_to_file(str(test_file), "Third line\n")
    
    # Verify content
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "Initial content\n" + "Second line\n" + "Third line\n"

def test_file_not_found():
    # Attempt to append to a non-existent file
    with pytest.raises(FileNotFoundError):
        append_text_to_file("non_existent_file.txt", "Some text")

def test_invalid_file_path_type():
    # Test with non-string file path
    with pytest.raises(TypeError):
        append_text_to_file(123, "Some text")

def test_invalid_text_type():
    # Test with non-string text to append
    with pytest.raises(TypeError):
        append_text_to_file("test.txt", 456)