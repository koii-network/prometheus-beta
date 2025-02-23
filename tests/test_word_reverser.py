import pytest
from src.word_reverser import reverse_words

def test_basic_word_reversal():
    """Test basic word reversal"""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_words():
    """Test reversal of multiple words"""
    assert reverse_words("Python is awesome") == "awesome is Python"

def test_single_word():
    """Test input with a single word"""
    assert reverse_words("Hello") == "Hello"

def test_empty_string():
    """Test empty string input"""
    assert reverse_words("") == ""

def test_multiple_spaces():
    """Test handling of multiple spaces between words"""
    assert reverse_words("  Hello   World  ") == "World Hello"

def test_none_input():
    """Test None input"""
    assert reverse_words(None) == ""