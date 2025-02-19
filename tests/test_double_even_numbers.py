import pytest
from src.double_even_numbers import double_even_numbers

def test_double_even_numbers_standard_case():
    """Test that even numbers are doubled and odd numbers remain unchanged."""
    input_list = [1, 2, 3, 4, 5, 6]
    expected_output = [1, 4, 3, 8, 5, 12]
    assert double_even_numbers(input_list) == expected_output

def test_double_even_numbers_empty_list():
    """Test that an empty list returns an empty list."""
    assert double_even_numbers([]) == []

def test_double_even_numbers_only_odd():
    """Test a list with only odd numbers remains unchanged."""
    input_list = [1, 3, 5, 7]
    assert double_even_numbers(input_list) == input_list

def test_double_even_numbers_only_even():
    """Test a list with only even numbers gets doubled."""
    input_list = [2, 4, 6, 8]
    expected_output = [4, 8, 12, 16]
    assert double_even_numbers(input_list) == expected_output

def test_double_even_numbers_negative_numbers():
    """Test function works with negative numbers."""
    input_list = [-2, -3, 0, 1, 4]
    expected_output = [-4, -3, 0, 1, 8]
    assert double_even_numbers(input_list) == expected_output