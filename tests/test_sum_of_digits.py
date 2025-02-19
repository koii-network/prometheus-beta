import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits():
    # Test with all digits
    assert sum_of_digits('1234567890') == 45
    
    # Test with mixed alphanumeric string
    assert sum_of_digits('abc123') == 6
    
    # Test with no digits
    assert sum_of_digits('abcdef') == 0
    
    # Test with leading zeros
    assert sum_of_digits('00123') == 6
    
    # Test with empty string
    assert sum_of_digits('') == 0
    
    # Test with special characters
    assert sum_of_digits('a1b2c3!@#$%^&*()') == 6