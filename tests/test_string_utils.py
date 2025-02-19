import pytest
from src.string_utils import reverse_words

def test_reverse_words_basic():
    """Test basic word reversal"""
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_multiple_spaces():
    """Test handling of multiple spaces between words"""
    assert reverse_words("hello   world  python") == "python world hello"

def test_reverse_words_leading_trailing_spaces():
    """Test handling of leading and trailing spaces"""
    assert reverse_words("  hello world  ") == "world hello"

def test_reverse_words_empty_string():
    """Test handling of empty string"""
    assert reverse_words("") == ""

def test_reverse_words_single_word():
    """Test handling of single word"""
    assert reverse_words("hello") == "hello"

def test_reverse_words_with_punctuation():
    """Test handling of words with punctuation"""
    assert reverse_words("hello, world!") == "world hello"