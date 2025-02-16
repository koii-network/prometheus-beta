import pytest
from src.palindrome_number import is_palindrome_number

def test_palindrome_number_positive():
    """Test palindrome numbers."""
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

def test_negative_input_numbers():
    """Test handling of negative input numbers."""
    assert is_palindrome_number(-121) == True
    assert is_palindrome_number(-11) == True
    assert is_palindrome_number(-12321) == True

def test_invalid_input():
    """Test invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome_number("123")
    
    with pytest.raises(TypeError):
        is_palindrome_number(3.14)
    
    with pytest.raises(TypeError):
        is_palindrome_number(None)