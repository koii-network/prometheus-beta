import os
import pytest
from src.file_utils import append_text_to_file

def test_append_text_to_existing_file(tmp_path):
    # Create a temporary file
    test_file = tmp_path / "test_append.txt"
    test_file.write_text("Initial content\n")
    
    # Append text
    append_text_to_file(str(test_file), "Additional text")
    
    # Check content
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == "Initial content\nAdditional text"

def test_append_to_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Append text
    append_text_to_file(str(test_file), "First content")
    
    # Check content
    with open(test_file, 'r') as f:
        content = f.read()
    assert content == "First content"

def test_append_raises_filenotfound_error():
    with pytest.raises(FileNotFoundError):
        append_text_to_file("nonexistent_file.txt", "Some text")

def test_append_raises_type_error():
    with pytest.raises(TypeError):
        append_text_to_file(123, "Some text")
    
    with pytest.raises(TypeError):
        append_text_to_file("test.txt", 456)