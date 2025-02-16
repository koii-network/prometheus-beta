import pytest
from src.palindrome_check import is_palindrome_number

def test_palindrome_positive_numbers():
    """Test palindrome numbers"""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(1) == True
    assert is_palindrome_number(0) == True

def test_palindrome_negative_numbers():
    """Test palindrome numbers that are negative"""
    assert is_palindrome_number(-121) == True
    assert is_palindrome_number(-11) == True

def test_non_palindrome_numbers():
    """Test non-palindrome numbers"""
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(1234) == False
    assert is_palindrome_number(-123) == False

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    with pytest.raises(TypeError):
        is_palindrome_number(None)