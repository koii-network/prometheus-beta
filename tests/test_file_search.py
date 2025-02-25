import os
import pytest
from src.file_search import search_string_in_file

# Fixture to create a test file
@pytest.fixture
def sample_file(tmp_path):
    # Create a temporary file for testing
    d = tmp_path / "test_files"
    d.mkdir()
    file_path = d / "sample.txt"
    file_path.write_text("""Hello, world!
This is a test file.
Another line with world in it.
Testing search functionality.
world appears multiple times.""")
    return str(file_path)

def test_basic_string_search(sample_file):
    """Test basic string search functionality"""
    results = search_string_in_file(sample_file, "world")
    assert results == [1, 3, 5], "Should find 'world' on lines 1, 3, and 5"

def test_case_sensitive_search(sample_file):
    """Test case-sensitive search"""
    results = search_string_in_file(sample_file, "World")
    assert results == [], "Should return empty list for case-sensitive search"

def test_full_line_match(sample_file):
    """Test searching for a full line"""
    results = search_string_in_file(sample_file, "This is a test file.")
    assert results == [2], "Should find the exact line"

def test_no_matches(sample_file):
    """Test when no matches are found"""
    results = search_string_in_file(sample_file, "nonexistent")
    assert results == [], "Should return empty list when no matches"

def test_invalid_file_path():
    """Test handling of non-existent file"""
    with pytest.raises(FileNotFoundError):
        search_string_in_file("nonexistent_file.txt", "test")

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        search_string_in_file(123, "test")
    
    with pytest.raises(TypeError):
        search_string_in_file("file.txt", 123)

def test_empty_search_string(sample_file):
    """Test handling of empty search string"""
    with pytest.raises(ValueError):
        search_string_in_file(sample_file, "")