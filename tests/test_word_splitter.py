import pytest
from src.word_splitter import count_words

def test_default_separator():
    """Test counting words with default space separator."""
    assert count_words("hello world python") == 3
    assert count_words("  hello   world  python  ") == 3

def test_custom_separator():
    """Test counting words with custom separator."""
    assert count_words("apple,banana,cherry", separator=',') == 3
    assert count_words("one::two::three", separator='::') == 3

def test_empty_string():
    """Test empty string returns zero words."""
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_single_word():
    """Test strings with a single word."""
    assert count_words("hello") == 1
    assert count_words("hello", separator=',') == 1

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words(123)
    
    with pytest.raises(TypeError, match="Separator must be a string"):
        count_words("hello", separator=123)

def test_consecutive_separators():
    """Test handling of consecutive separators."""
    assert count_words("one,,two,,three", separator=',,') == 3
    assert count_words("  hello    world  python  ") == 3