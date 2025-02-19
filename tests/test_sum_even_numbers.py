import pytest
from src.sum_even_numbers import sum_even_numbers

def test_sum_even_numbers_normal_case():
    """Test with a mix of even and odd numbers"""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_sum_even_numbers_only_even():
    """Test with only even numbers"""
    assert sum_even_numbers([2, 4, 6, 8]) == 20

def test_sum_even_numbers_only_odd():
    """Test with only odd numbers"""
    assert sum_even_numbers([1, 3, 5, 7]) == 0

def test_sum_even_numbers_empty_list():
    """Test with an empty list"""
    assert sum_even_numbers([]) == 0

def test_sum_even_numbers_negative_numbers():
    """Test with negative even and odd numbers"""
    assert sum_even_numbers([-1, -2, -3, -4, 0, 1, 2]) == -4

def test_sum_even_numbers_invalid_input_non_list():
    """Test with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_even_numbers("not a list")

def test_sum_even_numbers_invalid_input_non_integers():
    """Test with list containing non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_even_numbers([1, 2, "3", 4])