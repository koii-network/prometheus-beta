import pytest
from src.word_char_reverser import reverse_words_and_chars

def test_multiple_words():
    """Test reversing multiple words."""
    assert reverse_words_and_chars("Hello World") == "dlroW olleH"
    assert reverse_words_and_chars("Python is awesome") == "emosewa si nohtyP"

def test_single_word():
    """Test reversing a single word."""
    assert reverse_words_and_chars("Hello") == "olleH"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words_and_chars("") == ""

def test_multiple_spaces():
    """Test handling of multiple spaces between words."""
    assert reverse_words_and_chars("  Hello   World  ") == "dlroW olleH"

def test_single_character_words():
    """Test handling of single-character words."""
    assert reverse_words_and_chars("a b c") == "c b a"

def test_mixed_case():
    """Test handling of mixed case words."""
    assert reverse_words_and_chars("Hello WORLD Python") == "nohtyP DLROW olleH"