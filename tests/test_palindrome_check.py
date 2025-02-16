import pytest
from src.palindrome_check import is_palindrome_number

def test_palindrome_positive_numbers():
    # Test known palindrome numbers
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True

def test_palindrome_negative_numbers():
    # Test palindrome with negative numbers
    assert is_palindrome_number(-121) == True
    assert is_palindrome_number(-11) == True

def test_non_palindrome_numbers():
    # Test non-palindrome numbers
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(1234) == False

def test_single_digit_numbers():
    # Test single digit numbers
    for i in range(10):
        assert is_palindrome_number(i) == True

def test_zero():
    # Special test for zero
    assert is_palindrome_number(0) == True

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        is_palindrome_number("123")
    with pytest.raises(TypeError):
        is_palindrome_number(3.14)
    with pytest.raises(TypeError):
        is_palindrome_number([121])