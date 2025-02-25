import os
import pytest
from src.file_reader import read_file_contents

def test_read_existing_file(tmp_path):
    # Create a temporary file with known content
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!\nThis is a test file."
    test_file.write_text(test_content)
    
    # Read the file
    result = read_file_contents(str(test_file))
    assert result == test_content

def test_read_nonexistent_file():
    # Test reading a file that does not exist
    with pytest.raises(FileNotFoundError):
        read_file_contents("nonexistent_file.txt")

def test_read_empty_file(tmp_path):
    # Create an empty temporary file
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    
    # Read the empty file
    result = read_file_contents(str(test_file))
    assert result == ""

def test_file_permissions(tmp_path, monkeypatch):
    # Simulate a permission error
    def mock_open(*args, **kwargs):
        raise PermissionError("Mocked permission error")
    
    monkeypatch.setattr('builtins.open', mock_open)
    
    # Create a dummy path
    test_file = tmp_path / "permission_test.txt"
    test_file.touch()
    
    # Verify that PermissionError is raised
    with pytest.raises(PermissionError):
        read_file_contents(str(test_file))

def test_unicode_file_contents(tmp_path):
    # Create a file with unicode characters
    test_file = tmp_path / "unicode_file.txt"
    test_content = "Hello, ä¸ç! ããã«ã¡ã¯"
    test_file.write_text(test_content, encoding='utf-8')
    
    # Read the file
    result = read_file_contents(str(test_file))
    assert result == test_content