import pytest
from src.string_splitter import count_words_by_separator

def test_default_separator():
    """Test default space separator"""
    assert count_words_by_separator("hello world") == 2
    assert count_words_by_separator("  hello   world  ") == 2

def test_custom_separator():
    """Test custom separator"""
    assert count_words_by_separator("apple,banana,cherry", ',') == 3
    assert count_words_by_separator("a::b::c", '::') == 3

def test_empty_string():
    """Test empty string input"""
    assert count_words_by_separator("") == 0
    assert count_words_by_separator("", ',') == 0

def test_string_with_only_separators():
    """Test string containing only separators"""
    assert count_words_by_separator("   ") == 0
    assert count_words_by_separator(",,,,", ',') == 0

def test_error_handling():
    """Test error cases"""
    # Non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        count_words_by_separator(123)
    
    # Non-string separator
    with pytest.raises(TypeError, match="Separator must be a string"):
        count_words_by_separator("hello", 123)
    
    # Empty separator
    with pytest.raises(ValueError, match="Separator cannot be an empty string"):
        count_words_by_separator("hello", '')