import os
import pytest
from src.file_reader import read_text_file

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, this is a test file!"
    test_file.write_text(test_content)
    
    # Read the file and check contents
    result = read_text_file(str(test_file))
    assert result == test_content

def test_read_nonexistent_file():
    # Test that FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError, match="The file non_existent_file.txt was not found."):
        read_text_file("non_existent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    result = read_text_file(str(test_file))
    assert result == ""

def test_read_file_with_unicode(tmp_path):
    # Create a file with unicode characters
    test_file = tmp_path / "unicode_file.txt"
    test_content = "Héllo, 世界! 🌍"
    test_file.write_text(test_content, encoding='utf-8')
    
    # Read the file and check contents
    result = read_text_file(str(test_file))
    assert result == test_content