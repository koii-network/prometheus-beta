import os
import pytest
from src.word_counter import count_words

def test_count_words_basic():
    # Create a test file
    test_file_path = 'tests/test_words.txt'
    with open(test_file_path, 'w') as f:
        f.write('apple, banana, apple, cherry, banana, apple')
    
    # Test the function
    word_counts, total_words = count_words(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Assertions
    assert word_counts == {'apple': 3, 'banana': 2, 'cherry': 1}
    assert total_words == 6

def test_count_words_single_word():
    # Create a test file with a single word
    test_file_path = 'tests/test_single_word.txt'
    with open(test_file_path, 'w') as f:
        f.write('hello')
    
    # Test the function
    word_counts, total_words = count_words(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Assertions
    assert word_counts == {'hello': 1}
    assert total_words == 1

def test_count_words_empty_file():
    # Create an empty test file
    test_file_path = 'tests/test_empty.txt'
    with open(test_file_path, 'w') as f:
        f.write('')
    
    # Test that the function raises a ValueError for an empty file
    with pytest.raises(ValueError, match="The file is empty"):
        count_words(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)

def test_count_words_nonexistent_file():
    # Test that the function raises a FileNotFoundError for a nonexistent file
    with pytest.raises(FileNotFoundError):
        count_words('tests/nonexistent_file.txt')

def test_count_words_multiple_spaces_and_commas():
    # Create a test file with multiple spaces and commas
    test_file_path = 'tests/test_spaces_commas.txt'
    with open(test_file_path, 'w') as f:
        f.write('hello,  world,hello, python,   hello')
    
    # Test the function
    word_counts, total_words = count_words(test_file_path)
    
    # Clean up the test file
    os.remove(test_file_path)
    
    # Assertions
    assert word_counts == {'hello': 3, 'world': 1, 'python': 1}
    assert total_words == 5