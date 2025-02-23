import pytest
from src.vowel_rotator import rotate_vowels

def test_basic_vowel_rotation():
    """Test basic vowel rotation"""
    assert rotate_vowels("hello") == "holli"
    assert rotate_vowels("world") == "werld"

def test_uppercase_vowel_rotation():
    """Test rotation of uppercase vowels"""
    assert rotate_vowels("AEIOU") == "EIOUA"
    assert rotate_vowels("HELLO") == "HOLLI"

def test_mixed_case_rotation():
    """Test rotation of mixed case strings"""
    assert rotate_vowels("Python") == "Pythen"
    assert rotate_vowels("OpenAI") == "Eponal"

def test_no_vowels():
    """Test strings with no vowels"""
    assert rotate_vowels("rhythm") == "rhythm"
    assert rotate_vowels("sky") == "sky"

def test_empty_string():
    """Test empty string input"""
    assert rotate_vowels("") == ""

def test_all_vowels():
    """Test strings with only vowels"""
    assert rotate_vowels("aeiou") == "eioua"
    assert rotate_vowels("AEIOU") == "EIOUA"

def test_special_characters():
    """Test strings with special characters and numbers"""
    assert rotate_vowels("h3ll0!") == "h3ll0!"
    assert rotate_vowels("a1e2i3o4u5") == "e1i2o3u4a5"