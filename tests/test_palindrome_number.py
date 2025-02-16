import pytest
from src.palindrome_number import is_palindrome_number

def test_palindrome_positive_numbers():
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True

def test_palindrome_negative_numbers():
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(-11) == True

def test_palindrome_single_digit():
    for i in range(10):
        assert is_palindrome_number(i) == True

def test_non_palindrome_numbers():
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(456) == False

def test_zero():
    assert is_palindrome_number(0) == True

def test_invalid_input():
    with pytest.raises(TypeError):
        is_palindrome_number("123")
    with pytest.raises(TypeError):
        is_palindrome_number(3.14)
    with pytest.raises(TypeError):
        is_palindrome_number(None)