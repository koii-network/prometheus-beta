import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_digit_sum_palindrome_positive_cases():
    """Test various positive cases of digit sum palindromes."""
    # Cases where sum of digits is a palindrome
    assert is_digit_sum_palindrome(56) == True   # 5+6 = 11 (palindrome)
    assert is_digit_sum_palindrome(11) == True   # 1+1 = 2 (palindrome)
    assert is_digit_sum_palindrome(99) == True   # 9+9 = 18 (not a palindrome)
    assert is_digit_sum_palindrome(0) == True    # 0 is a palindrome

def test_digit_sum_palindrome_negative_cases():
    """Test cases where sum of digits is not a palindrome."""
    assert is_digit_sum_palindrome(57) == False  # 5+7 = 12 (not a palindrome)
    assert is_digit_sum_palindrome(98) == False  # 9+8 = 17 (not a palindrome)

def test_digit_sum_palindrome_error_handling():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_digit_sum_palindrome(-5)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_digit_sum_palindrome("56")
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_digit_sum_palindrome(5.6)
    with pytest.raises(TypeError, match="Input must be an integer"):
        is_digit_sum_palindrome(None)