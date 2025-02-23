import os
import pytest
from src.file_string_replacer import replace_string_in_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file for testing"""
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello world! Hello Python! Hello universe!")
    return str(file_path)

def test_replace_string_successful(sample_file):
    """Test successful string replacement"""
    result = replace_string_in_file(sample_file, "Hello", "Hi")
    assert result is True
    
    with open(sample_file, 'r') as file:
        content = file.read()
        assert "Hi world! Hi Python! Hi universe!" == content

def test_replace_string_no_changes(sample_file):
    """Test when no replacements are made"""
    result = replace_string_in_file(sample_file, "Goodbye", "Hello")
    assert result is False

def test_replace_with_empty_string(sample_file):
    """Test replacing with an empty string"""
    result = replace_string_in_file(sample_file, "Hello ", "")
    assert result is True
    
    with open(sample_file, 'r') as file:
        content = file.read()
        assert "world!Pythonuniverse!" == content

def test_file_not_found():
    """Test handling of non-existent file"""
    with pytest.raises(FileNotFoundError):
        replace_string_in_file("nonexistent_file.txt", "old", "new")

def test_empty_file(tmp_path):
    """Test behavior with an empty file"""
    empty_file = tmp_path / "empty.txt"
    empty_file.touch()
    
    result = replace_string_in_file(str(empty_file), "test", "replacement")
    assert result is False