import pytest
from src.even_odd_processor import process_numbers

def test_process_numbers_mixed_list():
    """Test with a mixed list of even and odd numbers"""
    result = process_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_process_numbers_all_even():
    """Test with a list of only even numbers"""
    result = process_numbers([2, 4, 6, 8, 10])
    assert result == (30, 0)

def test_process_numbers_all_odd():
    """Test with a list of only odd numbers"""
    result = process_numbers([1, 3, 5, 7, 9])
    assert result == (0, 5)

def test_process_numbers_empty_list():
    """Test with an empty list"""
    result = process_numbers([])
    assert result == (0, 0)

def test_process_numbers_negative_numbers():
    """Test with negative numbers"""
    result = process_numbers([-1, -2, -3, -4, -5])
    assert result == (-6, 3)

def test_process_numbers_invalid_input():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list of numbers"):
        process_numbers("not a list")