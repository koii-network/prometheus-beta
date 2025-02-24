import os
import pytest
from src.file_writer import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    # Create a temporary file path
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    
    # Write to file
    write_string_to_file(str(test_file), test_content)
    
    # Verify file contents
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_overwrite(tmp_path):
    # Create a temporary file path
    test_file = tmp_path / "test_file.txt"
    
    # Write initial content
    write_string_to_file(str(test_file), "First content")
    
    # Overwrite with new content
    new_content = "Updated content"
    write_string_to_file(str(test_file), new_content)
    
    # Verify file contents are updated
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == new_content

def test_write_string_to_file_empty_string(tmp_path):
    # Create a temporary file path
    test_file = tmp_path / "test_file.txt"
    
    # Write empty string
    write_string_to_file(str(test_file), "")
    
    # Verify file is empty
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == ""

def test_write_string_to_file_invalid_file_path_type():
    # Test non-string file path
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    # Test non-string content
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_empty_file_path():
    # Test empty file path
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("   ", "content")
        
def test_write_string_to_file_non_existent_directory(tmp_path):
    # Test writing to a non-existent directory
    non_existent_path = tmp_path / "non_existent_dir" / "test.txt"
    
    with pytest.raises(IOError):
        write_string_to_file(str(non_existent_path), "content")