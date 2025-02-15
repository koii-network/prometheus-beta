import pytest
from src.palindrome_check import is_palindrome_number

def test_palindrome_number_positive():
    """Test positive cases of palindrome numbers."""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(1) == True

def test_palindrome_number_negative():
    """Test non-palindrome numbers."""
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(456) == False
    assert is_palindrome_number(10) == False

def test_palindrome_number_with_negative_input():
    """Test palindrome numbers with negative signs."""
    assert is_palindrome_number(-121) == True
    assert is_palindrome_number(-11) == True

def test_palindrome_number_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    with pytest.raises(TypeError):
        is_palindrome_number(None)