import os
import pytest
from src.file_string_search import search_string_in_file

def test_search_string_exists():
    # Create a temporary test file
    test_file_path = 'tests/test_search_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello world\n")
        f.write("This is a test file\n")
        f.write("Hello again\n")
    
    try:
        # Search for existing string
        result = search_string_in_file(test_file_path, 'Hello')
        assert result == [1, 3], "Should find 'Hello' on lines 1 and 3"
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_search_string_not_exists():
    # Create a temporary test file
    test_file_path = 'tests/test_search_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("This is a test file\n")
    
    try:
        # Search for non-existing string
        result = search_string_in_file(test_file_path, 'hello')
        assert result == [], "Should return empty list for non-existing string"
    finally:
        # Clean up test file
        os.remove(test_file_path)

def test_search_string_empty_file():
    # Create an empty test file
    test_file_path = 'tests/test_search_file.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    try:
        # Search in empty file
        result = search_string_in_file(test_file_path, 'test')
        assert result == [], "Should return empty list for empty file"
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