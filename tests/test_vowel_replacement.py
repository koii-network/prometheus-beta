import pytest
from src.vowel_replacement import replace_vowels

def test_replace_vowels_basic():
    """Test basic vowel replacement"""
    assert replace_vowels('hello') == 'holli'
    assert replace_vowels('world') == 'wirld'

def test_replace_vowels_uppercase():
    """Test vowel replacement with uppercase letters"""
    assert replace_vowels('HELLO') == 'HOLLI'
    assert replace_vowels('WORLD') == 'WIRLD'

def test_replace_vowels_mixed_case():
    """Test vowel replacement with mixed case"""
    assert replace_vowels('Hello World') == 'Holli Wirld'

def test_replace_vowels_full_cycle():
    """Test that vowels cycle through a, e, i, o, u"""
    assert replace_vowels('aeiou') == 'eioua'
    assert replace_vowels('AEIOU') == 'EIOUA'

def test_replace_vowels_no_vowels():
    """Test string with no vowels"""
    assert replace_vowels('rhythm') == 'rhythm'

def test_replace_vowels_empty_string():
    """Test empty string"""
    assert replace_vowels('') == ''

def test_replace_vowels_special_characters():
    """Test string with special characters and numbers"""
    assert replace_vowels('a1b2c3!@#') == 'e1b2c3!@#'