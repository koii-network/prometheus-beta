import pytest
from src.word_counter import count_unique_words

def test_count_unique_words():
    # Basic case
    assert count_unique_words("Hello world hello") == 2
    
    # Case insensitivity
    assert count_unique_words("Hello HELLO hello") == 1
    
    # Punctuation handling
    assert count_unique_words("Hello, world! Hello, there.") == 3
    
    # Empty string
    assert count_unique_words("") == 0
    
    # String with only punctuation
    assert count_unique_words("!@#$%^&*()") == 0
    
    # Multiple spaces and punctuation
    assert count_unique_words("  hello   world!  Hello?  ") == 2
    
    # Sentences with repeated words
    text = "The quick brown fox jumps over the lazy dog. The dog barks."
    assert count_unique_words(text) == 9