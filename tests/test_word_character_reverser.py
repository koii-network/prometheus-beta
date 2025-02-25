import pytest
from src.word_character_reverser import reverse_word_characters

def test_basic_sentence_reversal():
    """Test reversing characters in a basic sentence."""
    assert reverse_word_characters("hello world") == "olleh dlrow"

def test_multiple_word_sentence():
    """Test reversing characters in a multi-word sentence."""
    assert reverse_word_characters("Python is awesome") == "nohtyP si emosewa"

def test_empty_string():
    """Test handling of an empty string."""
    assert reverse_word_characters("") == ""

def test_single_word():
    """Test reversing a single word."""
    assert reverse_word_characters("python") == "nohtyp"

def test_sentence_with_punctuation():
    """Test a sentence with punctuation."""
    assert reverse_word_characters("hello, world!") == "olleh, dlrow!"

def test_sentence_with_mixed_case():
    """Test a sentence with mixed case words."""
    assert reverse_word_characters("Hello World") == "olleH dlroW"

def test_sentence_with_numbers():
    """Test a sentence with numbers."""
    assert reverse_word_characters("python 3.9 rocks") == "nohtyp 3.9 skcor"

def test_whitespace_handling():
    """Test handling of extra whitespace."""
    assert reverse_word_characters("  hello   world  ") == "olleh dlrow"