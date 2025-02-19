import os
import pytest
from src.word_list_processor import process_word_list

def test_process_word_list():
    # Create a temporary test file
    test_file_path = 'tests/test_words.txt'
    with open(test_file_path, 'w') as f:
        f.write("apple\nbanana\ncherry\napple\ndate\nbanana\negg")
    
    try:
        # Process the file
        result = process_word_list(test_file_path)
        
        # Check expected output
        expected = ['apple', 'banana', 'cherry', 'date', 'egg']
        assert result == expected, f"Expected {expected}, but got {result}"
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_words.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    try:
        # Process the empty file
        result = process_word_list(test_file_path)
        
        # Check that an empty list is returned
        assert result == [], f"Expected empty list, but got {result}"
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        process_word_list('tests/nonexistent_file.txt')

def test_single_word_file():
    # Create a single word test file
    test_file_path = 'tests/single_word.txt'
    with open(test_file_path, 'w') as f:
        f.write("hello")
    
    try:
        # Process the file
        result = process_word_list(test_file_path)
        
        # Check expected output
        assert result == ['hello'], f"Expected ['hello'], but got {result}"
    
    finally:
        # Clean up the test file
        os.remove(test_file_path)