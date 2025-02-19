import pytest
from src.even_sum import calculate_even_sum

def test_calculate_even_sum_basic():
    """Test basic functionality with even and odd numbers"""
    assert calculate_even_sum([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6

def test_calculate_even_sum_all_odd():
    """Test with only odd numbers"""
    assert calculate_even_sum([1, 3, 5, 7]) == 0

def test_calculate_even_sum_all_even():
    """Test with only even numbers"""
    assert calculate_even_sum([2, 4, 6, 8]) == 20

def test_calculate_even_sum_empty_list():
    """Test with an empty list"""
    assert calculate_even_sum([]) == 0

def test_calculate_even_sum_negative_numbers():
    """Test with negative even and odd numbers"""
    assert calculate_even_sum([-1, -2, -3, -4, 5, 6]) == 0

def test_calculate_even_sum_invalid_input_not_list():
    """Test with non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_even_sum("not a list")

def test_calculate_even_sum_invalid_input_non_integers():
    """Test with list containing non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_even_sum([1, 2, "3", 4])