import pytest
from src.palindrome_check import is_palindrome_number

def test_palindrome_positive_numbers():
    """Test positive palindrome numbers."""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True

def test_palindrome_negative_numbers():
    """Test negative palindrome numbers."""
    assert is_palindrome_number(-121) == False  # Minus sign prevents palindrome
    assert is_palindrome_number(-11) == False

def test_palindrome_single_digit():
    """Test single-digit numbers."""
    for i in range(10):
        assert is_palindrome_number(i) == True

def test_non_palindrome_numbers():
    """Test non-palindrome numbers."""
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(1234) == False
    assert is_palindrome_number(10) == False

def test_zero():
    """Test zero as a special case."""
    assert is_palindrome_number(0) == True

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    with pytest.raises(TypeError):
        is_palindrome_number(None)