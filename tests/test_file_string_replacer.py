import os
import pytest
from src.file_string_replacer import replace_string_in_file

def test_replace_string_in_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world! Hello Python! Hello world!")
    
    # Replace a string
    replacements = replace_string_in_file(str(test_file), "Hello", "Hi")
    
    # Check the result
    assert replacements == 3
    assert test_file.read_text() == "Hi world! Hi Python! Hi world!"

def test_replace_string_no_occurrences(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world!")
    
    # Replace a string that doesn't exist
    replacements = replace_string_in_file(str(test_file), "Python", "Java")
    
    # Check the result
    assert replacements == 0
    assert test_file.read_text() == "Hello world!"

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("non_existent_file.txt", "old", "new")

def test_replace_empty_string(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world!")
    
    # Replace with an empty string
    replacements = replace_string_in_file(str(test_file), "world", "")
    
    # Check the result
    assert replacements == 1
    assert test_file.read_text() == "Hello !"