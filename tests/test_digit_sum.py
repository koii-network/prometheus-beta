import pytest
from src.digit_sum import sum_of_digits

def test_sum_of_digits():
    # Test with only digits
    assert sum_of_digits('1234567890') == 45
    
    # Test with mixed string
    assert sum_of_digits('abc123') == 6
    
    # Test with empty string
    assert sum_of_digits('') == 0
    
    # Test with no digits
    assert sum_of_digits('abcdef') == 0
    
    # Test with leading zeros
    assert sum_of_digits('00123') == 6
    
    # Test with multiple digit occurrences
    assert sum_of_digits('a1b2c3') == 6
    
    # Test with special characters
    assert sum_of_digits('!@#$%1^&*2(3)') == 6