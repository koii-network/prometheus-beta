import os
import pytest
from src.file_string_search import search_string_in_file

# Fixture to create a test file for searching
@pytest.fixture
def sample_file(tmp_path):
    # Create a temporary file with some sample content
    test_file = tmp_path / "sample.txt"
    test_file.write_text("""Hello, world!
This is a test file.
Another line with test content.
And a final line for testing.""")
    return str(test_file)

def test_string_found_single_line(sample_file):
    """Test finding a string that exists in a single line"""
    result = search_string_in_file(sample_file, "test file")
    assert result == [2], "Should find the string in line 2"

def test_string_found_multiple_lines(sample_file):
    """Test finding a string that exists in multiple lines"""
    result = search_string_in_file(sample_file, "test")
    assert result == [2, 3], "Should find the string in lines 2 and 3"

def test_string_not_found(sample_file):
    """Test when the string is not in the file"""
    result = search_string_in_file(sample_file, "python")
    assert result == [], "Should return an empty list when string is not found"

def test_case_sensitive_search(sample_file):
    """Test that search is case-sensitive"""
    result = search_string_in_file(sample_file, "Test")
    assert result == [], "Should be case-sensitive"

def test_file_not_found():
    """Test that FileNotFoundError is raised for non-existent file"""
    with pytest.raises(FileNotFoundError):
        search_string_in_file("non_existent_file.txt", "test")

def test_invalid_file_path_type():
    """Test that TypeError is raised for non-string file path"""
    with pytest.raises(TypeError, match="file_path must be a string"):
        search_string_in_file(123, "test")

def test_invalid_search_string_type():
    """Test that TypeError is raised for non-string search string"""
    with pytest.raises(TypeError, match="search_string must be a string"):
        search_string_in_file("file.txt", 123)

def test_empty_search_string(sample_file):
    """Test that ValueError is raised for empty search string"""
    with pytest.raises(ValueError, match="search_string cannot be empty"):
        search_string_in_file(sample_file, "")