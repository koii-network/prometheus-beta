import pytest
from src.string_digit_checker import is_digit_string

def test_is_digit_string_with_digits():
    assert is_digit_string("12345") == True
    assert is_digit_string("0") == True
    assert is_digit_string("9876543210") == True

def test_is_digit_string_with_non_digits():
    assert is_digit_string("123abc") == False
    assert is_digit_string("abc") == False
    assert is_digit_string("") == False
    assert is_digit_string(" ") == False
    assert is_digit_string("12 34") == False

def test_is_digit_string_with_invalid_input():
    with pytest.raises(TypeError):
        is_digit_string(12345)
    with pytest.raises(TypeError):
        is_digit_string(None)
    with pytest.raises(TypeError):
        is_digit_string(["12345"])