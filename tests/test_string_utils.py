import pytest
from src.string_utils import reverse_words

def test_basic_word_reversal():
    """Test basic word reversal"""
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_words():
    """Test reversal of multiple words"""
    assert reverse_words("One Two Three Four") == "Four Three Two One"

def test_preserve_whitespace():
    """Test preservation of original whitespace"""
    assert reverse_words("  Hello   World  ") == "  World   Hello  "

def test_mixed_alphanumeric():
    """Test handling of strings with numbers"""
    assert reverse_words("Hello123 World456") == "World456 Hello123"

def test_single_word():
    """Test handling of a single word"""
    assert reverse_words("Hello") == "Hello"

def test_empty_string():
    """Test handling of empty string"""
    assert reverse_words("") == ""

def test_only_spaces():
    """Test handling of string with only spaces"""
    assert reverse_words("   ") == "   "

def test_non_string_input():
    """Test handling of non-string input"""
    assert reverse_words(None) is None
    assert reverse_words(123) == 123

def test_complex_spacing():
    """Test complex spacing scenarios"""
    assert reverse_words("First    Second") == "Second    First"

def test_special_characters():
    """Test handling of strings with special characters"""
    assert reverse_words("Hello! World?") == "World? Hello!"