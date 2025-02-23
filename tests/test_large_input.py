import pytest
from src.staircase_combinations import calculate_staircase_combinations

def test_large_input():
    """Test handling of large input lists"""
    # Create a list of 100 ones
    large_list = [1] * 100
    result = calculate_staircase_combinations(large_list)
    assert result > 0  # Should return a positive number

def test_single_element_list():
    """Test single element list"""
    assert calculate_staircase_combinations([1]) == 1

def test_max_length_list():
    """Test list with maximum allowed length and values"""
    max_list = [20] * 100
    result = calculate_staircase_combinations(max_list)
    assert result > 0