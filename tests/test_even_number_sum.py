import pytest
from src.even_number_sum import sum_even_numbers

def test_sum_even_numbers_basic():
    """Test basic functionality with a mix of even and odd numbers"""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6

def test_sum_even_numbers_empty_list():
    """Test with an empty list"""
    assert sum_even_numbers([]) == 0

def test_sum_even_numbers_only_odds():
    """Test with only odd numbers"""
    assert sum_even_numbers([1, 3, 5, 7]) == 0

def test_sum_even_numbers_only_evens():
    """Test with only even numbers"""
    assert sum_even_numbers([2, 4, 6, 8]) == 20

def test_sum_even_numbers_negative():
    """Test with negative even and odd numbers"""
    assert sum_even_numbers([-2, -1, 0, 1, 2]) == 0

def test_sum_even_numbers_invalid_input_type():
    """Test with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_even_numbers("not a list")

def test_sum_even_numbers_invalid_element_type():
    """Test with non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_even_numbers([1, 2, "3", 4])