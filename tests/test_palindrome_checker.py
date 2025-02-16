import pytest
from src.palindrome_checker import is_palindrome_number

def test_palindrome_numbers():
    # Test known palindrome numbers
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(54345) == True

def test_non_palindrome_numbers():
    # Test known non-palindrome numbers
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(1234) == False

def test_negative_numbers():
    # Test negative numbers (should return False)
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(-11) == False

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    with pytest.raises(TypeError):
        is_palindrome_number(None)