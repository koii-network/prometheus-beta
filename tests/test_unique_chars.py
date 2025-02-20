import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    assert extract_unique_chars("11223344") == "123"
    assert extract_unique_chars("9876543210") == "9876543210"
    assert extract_unique_chars("444555666") == "456"

def test_extract_unique_chars_empty_input():
    assert extract_unique_chars("") == ""
    assert extract_unique_chars(None) == ""

def test_extract_unique_chars_single_character():
    assert extract_unique_chars("5") == "5"

def test_extract_unique_chars_random_order():
    assert extract_unique_chars("121314151") == "12345"
    assert extract_unique_chars("987651234") == "98765123"

def test_extract_unique_chars_preserve_order():
    # Ensure the first occurrence of each character is preserved
    assert extract_unique_chars("123112233") == "123"
    assert extract_unique_chars("555444333") == "54"