import pytest
from src.vowel_replacer import replace_vowels

def test_replace_vowels_lowercase():
    """Test vowel replacement for lowercase strings."""
    assert replace_vowels("hello") == "hollo"
    assert replace_vowels("python") == "pythun"
    assert replace_vowels("aeiou") == "eioua"

def test_replace_vowels_uppercase():
    """Test vowel replacement for uppercase strings."""
    assert replace_vowels("HELLO") == "HOLLO"
    assert replace_vowels("PYTHON") == "PYTHUN"
    assert replace_vowels("AEIOU") == "EIOUA"

def test_replace_vowels_mixed_case():
    """Test vowel replacement for mixed-case strings."""
    assert replace_vowels("Hello World") == "Hollo Wurld"
    assert replace_vowels("AeIoU") == "EoIuA"

def test_replace_vowels_no_vowels():
    """Test strings without vowels."""
    assert replace_vowels("rhythm") == "rhythm"
    assert replace_vowels("123456") == "123456"

def test_replace_vowels_empty_string():
    """Test empty string input."""
    assert replace_vowels("") == ""

def test_replace_vowels_special_characters():
    """Test strings with special characters and spaces."""
    assert replace_vowels("a!b@c#d$e%") == "e!b@c#d$u%"
    assert replace_vowels("Hello, World!") == "Hollo, Wurld!"