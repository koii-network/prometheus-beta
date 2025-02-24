import pytest
from src.word_splitter import count_words

def test_default_separator():
    """Test default space separator"""
    assert count_words("hello world") == 2
    assert count_words("  hello   world  ") == 2

def test_custom_separator():
    """Test custom separator"""
    assert count_words("apple,banana,cherry", separator=",") == 3
    assert count_words("one:two:three", separator=":") == 3

def test_empty_string():
    """Test empty string handling"""
    assert count_words("") == 0

def test_single_word():
    """Test single word scenarios"""
    assert count_words("hello") == 1
    assert count_words("hello", separator=",") == 1

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words(123)
    
    with pytest.raises(TypeError, match="Separator must be a string"):
        count_words("hello", separator=123)

def test_empty_separator():
    """Test error handling for empty separator"""
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        count_words("hello", separator="")