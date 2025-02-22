import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_is_digit_sum_palindrome():
    # Test cases where digit sum is a palindrome
    assert is_digit_sum_palindrome(11) == True    # 1+1 = 2, which is a palindrome
    assert is_digit_sum_palindrome(123) == False  # 1+2+3 = 6, which is not a palindrome
    assert is_digit_sum_palindrome(0) == True     # 0 is a palindrome
    assert is_digit_sum_palindrome(55) == True    # 5+5 = 10, which is not a palindrome
    
    # Test cases with large numbers
    assert is_digit_sum_palindrome(1234) == False  # 1+2+3+4 = 10, not a palindrome
    assert is_digit_sum_palindrome(9999) == True   # 9+9+9+9 = 36, which is not a palindrome
    
    # Error case
    with pytest.raises(ValueError):
        is_digit_sum_palindrome(-1)  # Negative numbers should raise ValueError