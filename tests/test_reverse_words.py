import pytest
from src.reverse_words import reverse_words

def test_basic_reverse_words():
    """Test basic word reversal"""
    assert reverse_words("hello world") == "world hello"

def test_multiple_words():
    """Test reversal of multiple words"""
    assert reverse_words("python is awesome") == "awesome is python"

def test_multiple_spaces():
    """Test handling of multiple spaces between words"""
    assert reverse_words("  hello   world  ") == "world hello"

def test_empty_string():
    """Test empty string input"""
    assert reverse_words("") == ""

def test_single_word():
    """Test single word input"""
    assert reverse_words("hello") == "hello"

def test_complex_spacing():
    """Test complex spacing scenarios"""
    assert reverse_words("  one    two  three   ") == "three two one"