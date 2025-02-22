import pytest
from src.is_digit_string import is_digit_string

def test_is_digit_string():
    # Test valid digit strings
    assert is_digit_string('12345') == True
    assert is_digit_string('0') == True
    
    # Test invalid strings
    assert is_digit_string('') == False
    assert is_digit_string('123a') == False
    assert is_digit_string('a123') == False
    assert is_digit_string(' 123') == False
    assert is_digit_string('123 ') == False
    assert is_digit_string('-123') == False
    assert is_digit_string('3.14') == False
    
    # Test edge cases
    assert is_digit_string('00000') == True
    assert is_digit_string('9' * 1000) == True  # Long string of digits