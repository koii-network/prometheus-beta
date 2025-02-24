import pytest
from src.word_capitalizer import capitalize_words

def test_capitalize_words_normal_case():
    """Test capitalizing words in a normal sentence."""
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_multiple_words():
    """Test capitalizing words in a multi-word string."""
    assert capitalize_words("python programming language") == "Python Programming Language"

def test_capitalize_words_empty_string():
    """Test handling of an empty string."""
    assert capitalize_words("") == ""

def test_capitalize_words_single_word():
    """Test capitalizing a single word."""
    assert capitalize_words("hello") == "Hello"

def test_capitalize_words_already_capitalized():
    """Test a string that is already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_mixed_case():
    """Test a string with mixed case."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_capitalize_words_with_spaces():
    """Test a string with multiple spaces."""
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_with_punctuation():
    """Test a string with punctuation."""
    assert capitalize_words("hello, world!") == "Hello, World!"