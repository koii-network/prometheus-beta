import os
import pytest
from src.file_reader import read_text_file

def test_read_text_file_success(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, this is a test file!"
    test_file.write_text(test_content)
    
    # Read the file and verify content
    result = read_text_file(str(test_file))
    assert result == test_content

def test_read_text_file_not_found():
    # Verify FileNotFoundError is raised for non-existent file
    with pytest.raises(FileNotFoundError):
        read_text_file("non_existent_file.txt")

def test_read_text_file_empty():
    # Create an empty file and verify it can be read
    tmp_file = "/tmp/empty_file.txt"
    with open(tmp_file, 'w') as f:
        pass
    
    result = read_text_file(tmp_file)
    assert result == ""
    
    # Clean up
    os.unlink(tmp_file)

def test_read_text_file_unicode():
    # Test reading a file with unicode characters
    tmp_file = "/tmp/unicode_test.txt"
    unicode_content = "こんにちは World! 🌍"
    with open(tmp_file, 'w', encoding='utf-8') as f:
        f.write(unicode_content)
    
    result = read_text_file(tmp_file)
    assert result == unicode_content
    
    # Clean up
    os.unlink(tmp_file)