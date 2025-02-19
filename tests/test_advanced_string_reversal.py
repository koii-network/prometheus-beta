import pytest
from src.advanced_string_reversal import advanced_string_reversal

def test_basic_string_reversal():
    assert advanced_string_reversal("hello") == "olleh"

def test_mixed_string_with_numbers():
    assert advanced_string_reversal("h3llo 123") == "olleh 321"

def test_palindrome_preservation():
    assert advanced_string_reversal("racecar is cool") == "racecar si looc"

def test_multiple_word_reversal():
    assert advanced_string_reversal("hello world") == "olleh dlrow"

def test_string_with_special_characters():
    assert advanced_string_reversal("hi123!world") == "ih321!dlrow"

def test_complex_mix():
    assert advanced_string_reversal("a1b2c3 level test") == "c1b2a3 level tset"

def test_empty_string():
    assert advanced_string_reversal("") == ""

def test_single_word():
    assert advanced_string_reversal("python") == "nohtyp"

def test_single_number():
    assert advanced_string_reversal("123") == "321"

def test_mixed_palindromes():
    assert advanced_string_reversal("racecar 12321 test") == "racecar 12321 tset"