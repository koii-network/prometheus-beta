import pytest
from src.palindrome_checker import is_palindrome_number

def test_palindrome_positive_numbers():
    """Test palindrome numbers with various positive integers."""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(1) == True
    
def test_non_palindrome_numbers():
    """Test non-palindrome numbers."""
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(1234) == False
    
def test_single_digit_numbers():
    """Test single-digit numbers."""
    for i in range(10):
        assert is_palindrome_number(i) == True
    
def test_zero():
    """Test zero specifically."""
    assert is_palindrome_number(0) == True
    
def test_negative_numbers():
    """Test negative numbers are not palindromes."""
    assert is_palindrome_number(-121) == False
    assert is_palindrome_number(-11) == False
    
def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    
    with pytest.raises(TypeError):
        is_palindrome_number(None)