import pytest
from src.palindrome_checker import is_palindrome_number

def test_is_palindrome_number():
    # Test positive palindrome numbers
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(11) == True
    assert is_palindrome_number(12321) == True
    
    # Test non-palindrome numbers
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(456) == False
    
    # Test zero and single-digit numbers
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(5) == True
    
    # Test negative numbers (absolute value considered)
    assert is_palindrome_number(-121) == True
    assert is_palindrome_number(-12321) == True
    
    # Test error handling
    with pytest.raises(TypeError):
        is_palindrome_number("123")
    
    with pytest.raises(TypeError):
        is_palindrome_number(12.34)
    
    with pytest.raises(TypeError):
        is_palindrome_number(None)