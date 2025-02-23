import os
import pytest
from src.file_search import search_string_in_file

@pytest.fixture
def sample_file(tmpdir):
    """Create a temporary sample file for testing."""
    test_file = tmpdir.join("sample.txt")
    test_file.write("Hello world\nThis is a test file\nWith multiple lines\nHello again")
    return str(test_file)

def test_successful_string_search(sample_file):
    """Test finding a string that exists in the file."""
    results = search_string_in_file(sample_file, "Hello")
    assert results == [1, 4]

def test_single_match(sample_file):
    """Test finding a string with a single match."""
    results = search_string_in_file(sample_file, "test file")
    assert results == [2]

def test_no_match(sample_file):
    """Test when the string is not found in the file."""
    results = search_string_in_file(sample_file, "python")
    assert results == []

def test_case_sensitive_search(sample_file):
    """Test that search is case-sensitive."""
    results = search_string_in_file(sample_file, "hello")
    assert results == []

def test_file_not_found():
    """Test behavior when file does not exist."""
    with pytest.raises(FileNotFoundError):
        search_string_in_file("non_existent_file.txt", "test")

def test_invalid_file_path_type():
    """Test behavior with invalid file path type."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        search_string_in_file(123, "test")

def test_invalid_search_string_type():
    """Test behavior with invalid search string type."""
    with pytest.raises(TypeError, match="search_string must be a string"):
        search_string_in_file("file.txt", 123)

def test_empty_search_string(sample_file):
    """Test behavior with empty search string."""
    with pytest.raises(ValueError, match="search_string cannot be empty"):
        search_string_in_file(sample_file, "")