import os
import pytest
import tempfile

from src.file_writer import write_string_to_file

def test_write_string_to_file():
    """Test writing a string to a file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test.txt')
        test_content = "Hello, World!"
        
        write_string_to_file(test_file, test_content)
        
        with open(test_file, 'r') as file:
            assert file.read() == test_content

def test_write_string_to_file_append():
    """Test appending a string to a file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test.txt')
        
        # First write
        write_string_to_file(test_file, "First line\n")
        
        # Append to the file
        write_string_to_file(test_file, "Second line\n", mode='a')
        
        with open(test_file, 'r') as file:
            content = file.read()
            assert content == "First line\n" + "Second line\n"

def test_write_string_to_file_invalid_path_type():
    """Test that a TypeError is raised for non-string file path."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    """Test that a TypeError is raised for non-string content."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_empty_path():
    """Test that a ValueError is raised for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("", "content")