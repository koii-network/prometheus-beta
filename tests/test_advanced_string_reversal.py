import pytest
from src.advanced_string_reversal import advanced_string_reversal

def test_basic_string_reversal():
    assert advanced_string_reversal("hello") == "olleh"

def test_numeric_reversal():
    assert advanced_string_reversal("hello123") == "olleh321"

def test_palindrome_preservation():
    assert advanced_string_reversal("racecar") == "racecar"

def test_mixed_content():
    assert advanced_string_reversal("hello 123 world") == "olleh 321 dlrow"

def test_complex_mixed_content():
    assert advanced_string_reversal("abc123def456") == "cba321fed654"

def test_punctuation_preservation():
    assert advanced_string_reversal("hello, world! 123") == "olleh, dlrow! 321"

def test_empty_string():
    assert advanced_string_reversal("") == ""

def test_single_character():
    assert advanced_string_reversal("a") == "a"

def test_multiple_palindromes():
    assert advanced_string_reversal("racecar hello level") == "racecar olleh level"