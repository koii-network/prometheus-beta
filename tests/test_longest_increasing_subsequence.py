import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_normal_case():
    """Test a typical increasing subsequence"""
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60]) == 5

def test_sorted_array():
    """Test a fully sorted array"""
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_reversed_array():
    """Test a reversed array"""
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_empty_array():
    """Test an empty array"""
    assert longest_increasing_subsequence([]) == 0

def test_single_element():
    """Test an array with a single element"""
    assert longest_increasing_subsequence([42]) == 1

def test_duplicate_elements():
    """Test an array with duplicate elements"""
    assert longest_increasing_subsequence([7, 7, 7, 7]) == 1

def test_mixed_elements():
    """Test an array with mixed increasing subsequences"""
    assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        longest_increasing_subsequence("not a list")

def test_invalid_input_non_integers():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        longest_increasing_subsequence([1, 2, "three", 4])