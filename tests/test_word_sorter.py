import os
import pytest
from src.word_sorter import process_word_list

def test_process_word_list_basic():
    # Create a test file with some words
    test_file_path = 'tests/test_words.txt'
    with open(test_file_path, 'w') as f:
        f.write("apple\nbanana\napple\ncherry\nbanana\ndate")
    
    # Process the file
    result = process_word_list(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Check the result
    assert result == ['apple', 'banana', 'cherry', 'date']

def test_process_word_list_empty_file():
    # Create an empty test file
    test_file_path = 'tests/empty_test_words.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    # Process the file
    result = process_word_list(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Check the result
    assert result == []

def test_process_word_list_case_insensitive():
    # Create a test file with mixed case words
    test_file_path = 'tests/case_test_words.txt'
    with open(test_file_path, 'w') as f:
        f.write("Apple\napple\nBanana\nbanana\nCHERRY\ncherry")
    
    # Process the file
    result = process_word_list(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Check the result
    assert result == ['apple', 'banana', 'cherry']

def test_process_word_list_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        process_word_list('non_existent_file.txt')

def test_process_word_list_whitespace_handling():
    # Create a test file with words with extra whitespace
    test_file_path = 'tests/whitespace_test_words.txt'
    with open(test_file_path, 'w') as f:
        f.write("  apple  \n banana \n  apple\n cherry ")
    
    # Process the file
    result = process_word_list(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Check the result
    assert result == ['apple', 'banana', 'cherry']