import os
import pytest
from src.file_append import append_text_to_file

def test_append_text_to_existing_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Initial content\n")
    
    # Append text
    append_text_to_file(str(test_file), "Additional text\n")
    
    # Check content
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "Initial content\nAdditional text\n"

def test_append_multiple_times(tmp_path):
    # Create a test file
    test_file = tmp_path / "multiple_append.txt"
    test_file.write_text("First line\n")
    
    # Append multiple times
    append_text_to_file(str(test_file), "Second line\n")
    append_text_to_file(str(test_file), "Third line\n")
    
    # Check content
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "First line\nSecond line\nThird line\n"

def test_append_to_nonexistent_file():
    # Attempt to append to a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        append_text_to_file("nonexistent_file.txt", "Some text")

def test_append_empty_string(tmp_path):
    # Test appending an empty string
    test_file = tmp_path / "empty_append.txt"
    test_file.write_text("Initial content\n")
    
    append_text_to_file(str(test_file), "")
    
    with open(test_file, 'r') as file:
        content = file.read()
        assert content == "Initial content\n"