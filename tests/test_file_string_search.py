import os
import pytest
from src.file_string_search import search_string_in_file

def test_search_string_in_file_found():
    # Create a test file
    test_file_path = 'test_search_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello world\n")
        f.write("This is a test\n")
        f.write("Hello again\n")
    
    try:
        # Test searching for an existing string
        result = search_string_in_file(test_file_path, 'Hello')
        assert result == [1, 3], "Should find 'Hello' on lines 1 and 3"
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_search_string_not_found():
    # Create a test file
    test_file_path = 'test_search_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello world\n")
    
    try:
        # Test searching for a non-existing string
        result = search_string_in_file(test_file_path, 'Python')
        assert result == [], "Should return empty list when string is not found"
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_search_string_file_not_found():
    # Test file not found error
    with pytest.raises(FileNotFoundError):
        search_string_in_file('non_existent_file.txt', 'test')

def test_search_string_invalid_input_types():
    # Test invalid input types
    with pytest.raises(TypeError):
        search_string_in_file(123, 'test')
    
    with pytest.raises(TypeError):
        search_string_in_file('file.txt', 123)