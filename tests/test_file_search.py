import os
import pytest
from src.file_search import search_string_in_file

def test_search_string_found(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello world\nThis is a test\nHello again")
    
    # Search for existing string
    results = search_string_in_file(str(test_file), "Hello")
    assert results == [1, 3], "Should find 'Hello' on lines 1 and 3"

def test_search_string_not_found(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Some random text\nAnother line")
    
    # Search for non-existing string
    results = search_string_in_file(str(test_file), "xyz")
    assert results == [], "Should return empty list when string not found"

def test_search_case_sensitive(tmp_path):
    # Create a temporary file for testing
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello Hello HELLO")
    
    # Check case sensitivity
    results_lowercase = search_string_in_file(str(test_file), "hello")
    results_mixed_case = search_string_in_file(str(test_file), "Hello")
    
    assert results_lowercase == [], "Should be case-sensitive"
    assert results_mixed_case == [1], "Should match exact case"

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        search_string_in_file("non_existent_file.txt", "test")