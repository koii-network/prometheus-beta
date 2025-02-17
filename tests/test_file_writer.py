import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    # Create a test file path
    test_file = tmp_path / "test_file.txt"
    
    # Content to write
    test_content = "Hello, World!"
    
    # Write the string to the file
    write_string_to_file(str(test_file), test_content)
    
    # Verify the file was created and contains the correct content
    assert test_file.exists()
    with open(test_file, 'r') as file:
        assert file.read() == test_content

def test_write_string_to_file_overwrite(tmp_path):
    # Create a test file path
    test_file = tmp_path / "test_file.txt"
    
    # Write initial content
    write_string_to_file(str(test_file), "Initial content")
    
    # Overwrite with new content
    new_content = "New content"
    write_string_to_file(str(test_file), new_content)
    
    # Verify the file contains only the new content
    with open(test_file, 'r') as file:
        assert file.read() == new_content

def test_write_string_to_file_invalid_file_path_type():
    # Test passing non-string file path
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    # Test passing non-string content
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_empty_file_path():
    # Test passing empty file path
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("  ", "content")
        write_string_to_file("", "content")