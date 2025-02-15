import pytest
from src.word_counter import count_words

def test_count_words():
    # Test normal case with multiple words
    assert count_words("Hello world") == 2
    
    # Test single word
    assert count_words("Python") == 1
    
    # Test empty string
    assert count_words("") == 0
    
    # Test string with multiple whitespaces
    assert count_words("  Hello   world  ") == 2
    
    # Test string with tabs and newlines
    assert count_words("Hello\tworld\ntest") == 3
    
    # Test None input
    assert count_words(None) == 0
    
    # Test string with only whitespace
    assert count_words("   \t\n  ") == 0
    
    # Test with special characters and punctuation
    assert count_words("Hello, world! How are you?") == 5