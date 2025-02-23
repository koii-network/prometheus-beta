import pytest
from src.string_word_splitter import split_and_count_words

def test_default_separator():
    """Test splitting with default space separator"""
    assert split_and_count_words("hello world python") == 3
    assert split_and_count_words("  hello   world  python  ") == 3

def test_custom_separator():
    """Test splitting with custom separator"""
    assert split_and_count_words("apple,banana,cherry", separator=",") == 3
    assert split_and_count_words("one::two::three", separator="::") == 3

def test_empty_string():
    """Test handling of empty string"""
    assert split_and_count_words("") == 0
    assert split_and_count_words("", separator=",") == 0

def test_no_separator_match():
    """Test when no separator is found in the string"""
    assert split_and_count_words("hello", separator=",") == 1

def test_consecutive_separators():
    """Test handling of consecutive separators"""
    assert split_and_count_words("a,,b,,c", separator=",,") == 3

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        split_and_count_words(123)
    
    with pytest.raises(TypeError, match="Separator must be a string"):
        split_and_count_words("hello", separator=123)

def test_empty_separator():
    """Test error handling for empty separator"""
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        split_and_count_words("hello", separator="")