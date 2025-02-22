import os
import pytest
from src.file_string_replacer import replace_string_in_file

def test_replace_string_in_file(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world! Hello universe! Hello everyone!")
    
    # Replace a substring
    replacements = replace_string_in_file(str(test_file), "Hello", "Hi")
    
    # Check the content
    assert test_file.read_text() == "Hi world! Hi universe! Hi everyone!"
    assert replacements == 3

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("nonexistent_file.txt", "old", "new")

def test_replace_empty_string(tmp_path):
    # Test replacing an empty string
    test_file = tmp_path / "empty_test.txt"
    test_file.write_text("Hello world!")
    
    replacements = replace_string_in_file(str(test_file), "", "prefix-")
    
    assert test_file.read_text() == "prefix-Hello world!"
    assert replacements == 0  # Empty string replacement returns 0

def test_no_replacements(tmp_path):
    # Test when no replacements are made
    test_file = tmp_path / "no_replace.txt"
    test_file.write_text("Hello world!")
    
    replacements = replace_string_in_file(str(test_file), "universe", "galaxy")
    
    assert test_file.read_text() == "Hello world!"
    assert replacements == 0