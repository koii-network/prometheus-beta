import os
import pytest
from src.word_frequency import count_word_frequencies

def test_normal_word_frequency():
    # Create a test file
    test_file_path = 'tests/test_input.txt'
    with open(test_file_path, 'w') as f:
        f.write('apple, banana, apple, cherry, banana, apple')
    
    # Expected result
    expected = {
        'apple': 3,
        'banana': 2,
        'cherry': 1
    }
    
    # Test the function
    result = count_word_frequencies(test_file_path)
    assert result == expected
    
    # Clean up
    os.remove(test_file_path)

def test_single_word():
    # Create a test file with a single word
    test_file_path = 'tests/test_input.txt'
    with open(test_file_path, 'w') as f:
        f.write('apple')
    
    # Expected result
    expected = {'apple': 1}
    
    # Test the function
    result = count_word_frequencies(test_file_path)
    assert result == expected
    
    # Clean up
    os.remove(test_file_path)

def test_multiple_spaces_and_commas():
    # Create a test file with multiple spaces and commas
    test_file_path = 'tests/test_input.txt'
    with open(test_file_path, 'w') as f:
        f.write('apple,  banana,   cherry,apple, banana')
    
    # Expected result
    expected = {
        'apple': 2,
        'banana': 2,
        'cherry': 1
    }
    
    # Test the function
    result = count_word_frequencies(test_file_path)
    assert result == expected
    
    # Clean up
    os.remove(test_file_path)

def test_empty_file():
    # Create an empty test file
    test_file_path = 'tests/test_input.txt'
    with open(test_file_path, 'w') as f:
        f.write('')
    
    # Test that an empty file raises a ValueError
    with pytest.raises(ValueError, match="The file is empty"):
        count_word_frequencies(test_file_path)
    
    # Clean up
    os.remove(test_file_path)

def test_nonexistent_file():
    # Test that a nonexistent file raises a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        count_word_frequencies('nonexistent_file.txt')

def test_empty_file_path():
    # Test that an empty file path raises a ValueError
    with pytest.raises(ValueError, match="File path cannot be empty"):
        count_word_frequencies('')