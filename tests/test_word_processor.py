import os
import pytest
from src.word_processor import process_word_file

def test_process_word_file_basic():
    # Create a test file with words
    test_file_path = 'tests/test_words.txt'
    with open(test_file_path, 'w') as f:
        f.write("apple\nbanana\ncherry\napple\ndate\nbanana")
    
    # Process the file
    result = process_word_file(test_file_path)
    
    # Expected sorted unique words
    expected = ['apple', 'banana', 'cherry', 'date']
    
    # Clean up test file
    os.remove(test_file_path)
    
    # Assert
    assert result == expected

def test_process_word_file_case_insensitive():
    # Create a test file with case variations
    test_file_path = 'tests/test_words_case.txt'
    with open(test_file_path, 'w') as f:
        f.write("Apple\napple\nBANANA\nbanana")
    
    # Process the file
    result = process_word_file(test_file_path)
    
    # Clean up test file
    os.remove(test_file_path)
    
    # Expected should be lowercase and unique
    expected = ['apple', 'banana']
    
    # Assert
    assert result == expected

def test_process_word_file_empty():
    # Create an empty test file
    test_file_path = 'tests/test_words_empty.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    # Process the file
    result = process_word_file(test_file_path)
    
    # Clean up test file
    os.remove(test_file_path)
    
    # Expected should be an empty list
    expected = []
    
    # Assert
    assert result == expected

def test_process_word_file_not_found():
    # Attempt to process a non-existent file
    with pytest.raises(FileNotFoundError):
        process_word_file('tests/non_existent_file.txt')

def test_process_word_file_whitespace():
    # Create a test file with whitespace
    test_file_path = 'tests/test_words_whitespace.txt'
    with open(test_file_path, 'w') as f:
        f.write("  apple  \n banana \n  apple")
    
    # Process the file
    result = process_word_file(test_file_path)
    
    # Clean up test file
    os.remove(test_file_path)
    
    # Expected should be sorted and trimmed
    expected = ['apple', 'banana']
    
    # Assert
    assert result == expected