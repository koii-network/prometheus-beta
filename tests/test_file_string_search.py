import os
import pytest
from src.file_string_search import search_string_in_file

def test_search_string_in_file_basic():
    # Create a temporary test file
    with open('test_file.txt', 'w') as f:
        f.write("Hello world\nThis is a test\nHello again")
    
    result = search_string_in_file('test_file.txt', 'Hello')
    assert result == [1, 3], "Should find 'Hello' on lines 1 and 3"
    
    # Clean up
    os.remove('test_file.txt')

def test_search_string_not_found():
    # Create a temporary test file
    with open('test_file.txt', 'w') as f:
        f.write("This is a test file\nWith no matching string")
    
    result = search_string_in_file('test_file.txt', 'Python')
    assert result == [], "Should return empty list when string is not found"
    
    # Clean up
    os.remove('test_file.txt')

def test_search_case_sensitive():
    # Create a temporary test file
    with open('test_file.txt', 'w') as f:
        f.write("Hello World\nhello world")
    
    result = search_string_in_file('test_file.txt', 'Hello')
    assert result == [1], "Should be case-sensitive"
    
    # Clean up
    os.remove('test_file.txt')

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        search_string_in_file('nonexistent_file.txt', 'test')

def test_invalid_input_types():
    with pytest.raises(TypeError):
        search_string_in_file(123, 'test')
    
    with pytest.raises(TypeError):
        search_string_in_file('file.txt', 123)

def test_empty_file():
    # Create an empty test file
    with open('empty_file.txt', 'w') as f:
        pass
    
    result = search_string_in_file('empty_file.txt', 'test')
    assert result == [], "Should return empty list for empty file"
    
    # Clean up
    os.remove('empty_file.txt')