import pytest
from src.max_sum_increasing_subsequence import max_sum_increasing_subsequence

def test_standard_case():
    """Test a standard case with increasing subsequences"""
    assert max_sum_increasing_subsequence([1, 101, 2, 3, 100]) == 106
    assert max_sum_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 255

def test_single_element():
    """Test case with a single element"""
    assert max_sum_increasing_subsequence([5]) == 5

def test_descending_sequence():
    """Test a descending sequence"""
    assert max_sum_increasing_subsequence([5, 4, 3, 2, 1]) == 5

def test_all_same_elements():
    """Test a sequence with all same elements"""
    assert max_sum_increasing_subsequence([7, 7, 7, 7]) == 7

def test_negative_numbers():
    """Test with negative numbers"""
    assert max_sum_increasing_subsequence([-5, -4, -3, -2, -1]) == -1
    assert max_sum_increasing_subsequence([-10, 5, -3, 7, 1]) == 10

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError):
        max_sum_increasing_subsequence([])