"""
Test module for word list processor functionality.
"""

import os
import pytest
from src.word_list_processor import process_word_list

# Helper function to create temporary test files
def create_test_file(filename, content):
    """Create a temporary test file with given content."""
    with open(filename, 'w') as f:
        f.write(content)

# Test cases
def test_process_word_list_basic():
    """Test basic functionality of processing a word list."""
    # Create a test file
    test_file = 'test_words.txt'
    create_test_file(test_file, 'apple\nbanana\napple\ncherry\nbanana')
    
    # Process the file
    result = process_word_list(test_file)
    
    # Assert expected output
    assert result == ['apple', 'banana', 'cherry']
    
    # Clean up
    os.remove(test_file)

def test_process_word_list_empty_file():
    """Test processing an empty file."""
    # Create an empty test file
    test_file = 'empty_test_words.txt'
    create_test_file(test_file, '')
    
    # Process the file
    result = process_word_list(test_file)
    
    # Assert empty list
    assert result == []
    
    # Clean up
    os.remove(test_file)

def test_process_word_list_whitespace_handling():
    """Test handling of whitespace and case-insensitivity."""
    # Create a test file with whitespace and mixed case
    test_file = 'whitespace_test_words.txt'
    create_test_file(test_file, '  Apple  \n Banana \n  apple\n BANANA  ')
    
    # Process the file
    result = process_word_list(test_file)
    
    # Assert expected output
    assert result == ['apple', 'banana']
    
    # Clean up
    os.remove(test_file)

def test_process_word_list_nonexistent_file():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        process_word_list('nonexistent_file.txt')

def test_process_word_list_invalid_input():
    """Test handling of invalid input type."""
    with pytest.raises(TypeError):
        process_word_list(123)  # Pass an integer instead of a string