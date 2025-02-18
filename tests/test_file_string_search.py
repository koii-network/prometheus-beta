import os
import pytest
from src.file_string_search import search_string_in_file

def test_search_string_in_file_multiple_matches():
    # Create a test file
    test_file_path = 'tests/test_search_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello world\n")
        f.write("This is a test file\n")
        f.write("Hello again world\n")
    
    try:
        # Search for 'Hello'
        results = search_string_in_file(test_file_path, 'Hello')
        assert results == [1, 3], "Should find 'Hello' on lines 1 and 3"
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_search_string_in_file_no_matches():
    # Create a test file
    test_file_path = 'tests/test_search_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("This is a test file\n")
        f.write("No matching string here\n")
    
    try:
        # Search for a non-existent string
        results = search_string_in_file(test_file_path, 'unique')
        assert results == [], "Should return an empty list when no matches"
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_search_string_case_sensitive():
    # Create a test file
    test_file_path = 'tests/test_search_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello World\n")
        f.write("hello world\n")
    
    try:
        # Case-sensitive search
        results = search_string_in_file(test_file_path, 'Hello')
        assert results == [1], "Should be case-sensitive"
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        search_string_in_file('non_existent_file.txt', 'test')

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        search_string_in_file(123, 'test')
    
    with pytest.raises(TypeError):
        search_string_in_file('file.txt', 123)