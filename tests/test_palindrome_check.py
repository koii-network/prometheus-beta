import pytest
from src.palindrome_check import is_palindrome_number

def test_palindrome_number_positive():
    """Test positive palindrome numbers."""
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(1) == True

def test_palindrome_number_negative():
    """Test non-palindrome numbers."""
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(1234) == False

def test_palindrome_number_large():
    """Test large palindrome and non-palindrome numbers."""
    assert is_palindrome_number(1234321) == True
    assert is_palindrome_number(12345678) == False

def test_palindrome_number_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        is_palindrome_number("121")
    
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    
    with pytest.raises(TypeError):
        is_palindrome_number(None)