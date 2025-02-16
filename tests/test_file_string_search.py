import pytest
import os
from src.file_string_search import search_string_in_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file for testing"""
    sample_text = """Hello, world!
This is a test file.
Search for something in this line.
Another line to test."""
    file_path = tmp_path / "sample.txt"
    file_path.write_text(sample_text)
    return str(file_path)

def test_search_string_exists(sample_file):
    """Test searching for existing string"""
    result = search_string_in_file(sample_file, "test")
    assert result == [2, 3]

def test_search_string_case_sensitive(sample_file):
    """Test case-sensitivity of search"""
    result = search_string_in_file(sample_file, "Test")
    assert result == []

def test_search_string_full_match(sample_file):
    """Test searching for full string"""
    result = search_string_in_file(sample_file, "This is a test file.")
    assert result == [2]

def test_search_string_no_match(sample_file):
    """Test when no matches are found"""
    result = search_string_in_file(sample_file, "nonexistent")
    assert result == []

def test_file_not_found():
    """Test behavior when file does not exist"""
    with pytest.raises(FileNotFoundError):
        search_string_in_file("nonexistent_file.txt", "test")

def test_invalid_file_path_type():
    """Test invalid file path type"""
    with pytest.raises(TypeError, match="file_path must be a string"):
        search_string_in_file(123, "test")

def test_invalid_search_string_type(sample_file):
    """Test invalid search string type"""
    with pytest.raises(TypeError, match="search_string must be a string"):
        search_string_in_file(sample_file, 123)