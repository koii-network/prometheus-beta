import pytest
from src.sum_unique_elements import sum_unique_elements

def test_sum_unique_elements_basic():
    """Test basic scenario with unique and duplicate elements"""
    assert sum_unique_elements([1, 2, 3, 2]) == 4  # unique elements are 1, 3
    assert sum_unique_elements([1, 1, 1, 1]) == 0  # no unique elements
    assert sum_unique_elements([1, 2, 3, 4]) == 10  # all elements are unique

def test_sum_unique_elements_empty():
    """Test empty array"""
    assert sum_unique_elements([]) == 0

def test_sum_unique_elements_negative_numbers():
    """Test with negative numbers"""
    assert sum_unique_elements([-1, -1, 2, 3]) == 4  # unique elements are -1, 2, 3
    assert sum_unique_elements([-1, -2, -1, -2]) == 0  # no unique elements

def test_sum_unique_elements_mixed_duplicates():
    """Test with multiple duplicates"""
    assert sum_unique_elements([1, 2, 2, 3, 3, 4]) == 5  # unique elements are 1, 4
    assert sum_unique_elements([1, 1, 2, 2, 3, 3]) == 0  # no unique elements

def test_sum_unique_elements_large_list():
    """Test with a larger list of numbers"""
    large_list = [1, 2, 3] * 100 + [4, 5, 6]
    assert sum_unique_elements(large_list) == 15  # unique elements are 4, 5, 6