import os
import pytest
from src.file_string_search import search_string_in_file

def test_search_string_in_file_basic():
    # Create a test file
    with open('test_search.txt', 'w') as f:
        f.write("Hello world\n")
        f.write("This is a test file\n")
        f.write("Hello again\n")
    
    try:
        # Test basic search
        results = search_string_in_file('test_search.txt', 'Hello')
        assert results == [1, 3], "Should find 'Hello' on lines 1 and 3"
        
        # Test case-sensitive search
        results = search_string_in_file('test_search.txt', 'hello')
        assert results == [], "Should return empty list for case-sensitive search"
    
    finally:
        # Clean up test file
        os.remove('test_search.txt')

def test_search_string_not_found():
    # Create a test file
    with open('test_search_not_found.txt', 'w') as f:
        f.write("Some content\n")
        f.write("Another line\n")
    
    try:
        # Test when string is not found
        results = search_string_in_file('test_search_not_found.txt', 'missing')
        assert results == [], "Should return empty list when string is not found"
    
    finally:
        # Clean up test file
        os.remove('test_search_not_found.txt')

def test_file_not_found():
    # Test FileNotFoundError
    with pytest.raises(FileNotFoundError):
        search_string_in_file('non_existent_file.txt', 'search')

def test_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        search_string_in_file(123, 'search')
    
    with pytest.raises(TypeError):
        search_string_in_file('file.txt', 123)