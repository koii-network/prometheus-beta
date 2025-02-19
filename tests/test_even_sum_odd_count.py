import pytest
from src.even_sum_odd_count import analyze_numbers

def test_mixed_numbers():
    # Test with a mix of even and odd numbers
    result = analyze_numbers([1, 2, 3, 4, 5, 6])
    assert result == (12, 3)

def test_all_even_numbers():
    # Test with only even numbers
    result = analyze_numbers([2, 4, 6, 8])
    assert result == (20, 0)

def test_all_odd_numbers():
    # Test with only odd numbers
    result = analyze_numbers([1, 3, 5, 7])
    assert result == (0, 4)

def test_empty_list():
    # Test with an empty list
    result = analyze_numbers([])
    assert result == (0, 0)

def test_negative_numbers():
    # Test with negative numbers
    result = analyze_numbers([-1, -2, -3, -4, 5, 6])
    assert result == (2, 3)

def test_zero_included():
    # Test with zero (which is considered even)
    result = analyze_numbers([0, 1, 2, 3])
    assert result == (2, 2)