import pytest
from src.digit_sum import sum_of_digits

def test_sum_of_digits_all_numbers():
    """Test with a string containing only numbers."""
    assert sum_of_digits('1234567890') == 45

def test_sum_of_digits_mixed_string():
    """Test with a string containing both letters and numbers."""
    assert sum_of_digits('abc123') == 6

def test_sum_of_digits_no_numbers():
    """Test with a string containing no numbers."""
    assert sum_of_digits('abcdef') == 0

def test_sum_of_digits_with_zeros():
    """Test with a string containing zeros."""
    assert sum_of_digits('a0b1c00d2') == 3

def test_sum_of_digits_empty_string():
    """Test with an empty string."""
    assert sum_of_digits('') == 0

def test_sum_of_digits_special_characters():
    """Test with a string containing special characters."""
    assert sum_of_digits('!@#$%123^&*()') == 6