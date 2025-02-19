import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_is_digit_sum_palindrome_positive_cases():
    # Test numbers where digit sum is a palindrome
    assert is_digit_sum_palindrome(11) == True   # 1+1 = 2
    assert is_digit_sum_palindrome(123) == True  # 1+2+3 = 6
    assert is_digit_sum_palindrome(5) == True    # Single digit sum
    assert is_digit_sum_palindrome(100) == True  # 1+0+0 = 1

def test_is_digit_sum_palindrome_negative_cases():
    # Test numbers where digit sum is not a palindrome
    assert is_digit_sum_palindrome(12) == False  # 1+2 = 3
    assert is_digit_sum_palindrome(9876) == False  # 9+8+7+6 = 30
    assert is_digit_sum_palindrome(56) == False  # 5+6 = 11

def test_is_digit_sum_palindrome_zero():
    # Test zero case
    assert is_digit_sum_palindrome(0) == True  # 0 is a palindrome

def test_is_digit_sum_palindrome_raises_on_negative():
    # Test negative number raises ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_digit_sum_palindrome(-5)

def test_is_digit_sum_palindrome_large_number():
    # Test a large number with palindrome digit sum
    assert is_digit_sum_palindrome(1234554321) == True  # Sum of digits is 22
    
def test_is_digit_sum_palindrome_complex_cases():
    # More complex test cases
    assert is_digit_sum_palindrome(1111) == True   # 1+1+1+1 = 4
    assert is_digit_sum_palindrome(9) == True      # Single digit