import pytest
from src.reverse_words import reverse_words

def test_basic_reverse():
    assert reverse_words("Hello World") == "World Hello"

def test_multiple_words():
    assert reverse_words("Python is awesome") == "awesome is Python"

def test_multiple_spaces():
    assert reverse_words("Hello   World  Test") == "Test World Hello"

def test_empty_string():
    assert reverse_words("") == ""

def test_single_word():
    assert reverse_words("Python") == "Python"

def test_whitespace_only():
    assert reverse_words("   ") == ""

def test_mixed_case():
    assert reverse_words("Hello WORLD Test") == "Test WORLD Hello"