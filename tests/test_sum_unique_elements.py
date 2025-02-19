import pytest
from src.sum_unique_elements import sum_unique_elements

def test_sum_unique_elements_basic():
    """Test basic functionality with mixed unique and duplicate elements"""
    assert sum_unique_elements([1, 2, 3, 2, 1, 4]) == 7  # 1+2+3+4

def test_sum_unique_elements_all_unique():
    """Test case where all elements are unique"""
    assert sum_unique_elements([1, 2, 3, 4, 5]) == 15

def test_sum_unique_elements_all_duplicates():
    """Test case where all elements are duplicates"""
    assert sum_unique_elements([1, 1, 1, 1]) == 0

def test_sum_unique_elements_empty_list():
    """Test empty list input"""
    assert sum_unique_elements([]) == 0

def test_sum_unique_elements_negative_numbers():
    """Test with negative numbers"""
    assert sum_unique_elements([-1, -2, -1, 3, 3]) == -3  # -1 + -2

def test_sum_unique_elements_mixed_positives_and_negatives():
    """Test with mixed positive and negative numbers"""
    assert sum_unique_elements([1, -1, 2, -2, 1, -1]) == 2  # 1 + 2 + -1