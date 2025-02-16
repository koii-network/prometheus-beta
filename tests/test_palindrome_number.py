import pytest
from src.palindrome_number import is_palindrome_number

def test_palindrome_number_positive():
    # Test positive palindrome numbers
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True

def test_palindrome_number_negative():
    # Test negative palindrome numbers
    assert is_palindrome_number(-121) == True
    assert is_palindrome_number(-11) == True

def test_non_palindrome_numbers():
    # Test non-palindrome numbers
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(456) == False

def test_single_digit_numbers():
    # Test single-digit numbers
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(5) == True
    assert is_palindrome_number(9) == True

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        is_palindrome_number("123")
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    with pytest.raises(TypeError):
        is_palindrome_number(None)