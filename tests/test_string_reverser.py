import pytest
from src.string_reverser import reverse_words_and_chars

def test_basic_reversal():
    """Test basic string reversal with multiple words."""
    assert reverse_words_and_chars("Hello World") == "dlroW olleH"

def test_single_word():
    """Test reversal of a single word."""
    assert reverse_words_and_chars("Python") == "nohtyP"

def test_empty_string():
    """Test handling of empty string."""
    assert reverse_words_and_chars("") == ""

def test_multiple_words():
    """Test reversal of multiple words."""
    assert reverse_words_and_chars("Python is awesome") == "emosewa si nohtyP"

def test_string_with_special_characters():
    """Test reversal with special characters."""
    assert reverse_words_and_chars("Hello, World!") == "!dlroW ,olleH"

def test_string_with_numbers():
    """Test reversal with numbers."""
    assert reverse_words_and_chars("Python 3.9 is great") == "taerg si 9.3 nohtyP"

def test_mixed_case():
    """Test reversal with mixed case."""
    assert reverse_words_and_chars("Hello OpenAI") == "IAnepO olleH"