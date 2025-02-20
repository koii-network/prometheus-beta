import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_normal_case():
    assert extract_unique_chars("11223344") == "123"
    assert extract_unique_chars("9876543210") == "9876543210"

def test_extract_unique_chars_empty_string():
    assert extract_unique_chars("") == ""

def test_extract_unique_chars_single_character():
    assert extract_unique_chars("5") == "5"

def test_extract_unique_chars_repeating_characters():
    assert extract_unique_chars("222333444") == "234"

def test_extract_unique_chars_completely_unique():
    assert extract_unique_chars("123456789") == "123456789"

def test_extract_unique_chars_invalid_input():
    with pytest.raises(TypeError):
        extract_unique_chars(12345)
    with pytest.raises(TypeError):
        extract_unique_chars(None)