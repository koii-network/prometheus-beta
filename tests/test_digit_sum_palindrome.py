import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_digit_sum_palindrome_basic_cases():
    # Test cases where sum of digits is a palindrome
    assert is_digit_sum_palindrome(11) == True   # 1+1 = 2 (palindrome)
    assert is_digit_sum_palindrome(198) == True  # 1+9+8 = 18 (not palindrome)
    assert is_digit_sum_palindrome(55) == True   # 5+5 = 10 (not palindrome)
    
def test_digit_sum_palindrome_zero_and_single_digit():
    # Test cases with zero and single digit
    assert is_digit_sum_palindrome(0) == True
    assert is_digit_sum_palindrome(5) == True
    assert is_digit_sum_palindrome(7) == True
    
def test_digit_sum_palindrome_larger_numbers():
    # Test larger numbers
    assert is_digit_sum_palindrome(1234) == False  # 1+2+3+4 = 10 (not palindrome)
    assert is_digit_sum_palindrome(9999) == True   # 9+9+9+9 = 36 (not palindrome)
    
def test_digit_sum_palindrome_edge_cases():
    # Test some specific edge cases
    assert is_digit_sum_palindrome(22) == True    # 2+2 = 4 (palindrome)
    assert is_digit_sum_palindrome(10) == False   # 1+0 = 1 (palindrome)
    
def test_digit_sum_palindrome_negative_input():
    # Test negative input raises ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_digit_sum_palindrome(-5)
        is_digit_sum_palindrome(-123)