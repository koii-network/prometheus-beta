import pytest
from src.unique_chars import extract_unique_chars

def test_extract_unique_chars_basic():
    assert extract_unique_chars("112233") == "123"
    assert extract_unique_chars("1122334455") == "12345"

def test_extract_unique_chars_complex():
    assert extract_unique_chars("9876543210") == "9876543210"
    assert extract_unique_chars("1234567890") == "1234567890"

def test_extract_unique_chars_edge_cases():
    assert extract_unique_chars("") == ""
    assert extract_unique_chars("11111") == "1"

def test_extract_unique_chars_error_handling():
    with pytest.raises(TypeError):
        extract_unique_chars(12345)
    with pytest.raises(TypeError):
        extract_unique_chars(None)