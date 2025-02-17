import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    test_file.write_text(test_content)
    
    # Read the file and verify contents
    result = read_file_contents(str(test_file))
    assert result == test_content

def test_read_nonexistent_file():
    # Verify FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty file and verify empty string is returned
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    result = read_file_contents(str(test_file))
    assert result == ""

def test_read_file_with_unicode(tmp_path):
    # Test reading a file with unicode characters
    test_file = tmp_path / "unicode_file.txt"
    unicode_content = "こんにちは世界 - Hello World in Japanese"
    test_file.write_text(unicode_content, encoding='utf-8')
    
    result = read_file_contents(str(test_file))
    assert result == unicode_content