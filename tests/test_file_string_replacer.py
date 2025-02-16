import os
import pytest
from src.file_string_replacer import replace_string_in_file

def test_replace_string_in_file(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("hello world, hello python, hello testing")
    
    # Test replacing a string
    replacements = replace_string_in_file(str(test_file), "hello", "hi")
    
    # Check the number of replacements and file contents
    assert replacements == 3
    assert test_file.read_text() == "hi world, hi python, hi testing"

def test_replace_empty_string(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_empty.txt"
    original_content = "hello world"
    test_file.write_text(original_content)
    
    # Test replacing an empty string
    replacements = replace_string_in_file(str(test_file), "", "")
    
    # Verify no changes were made
    assert replacements == 0
    assert test_file.read_text() == original_content

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("non_existent_file.txt", "old", "new")

def test_replace_with_empty_string(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_remove.txt"
    test_file.write_text("hello world, hello python")
    
    # Replace with empty string
    replacements = replace_string_in_file(str(test_file), "hello ", "")
    
    # Check the number of replacements and file contents
    assert replacements == 2
    assert test_file.read_text() == "world, python"