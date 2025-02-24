import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_strictly_increasing_sequence():
    """Test a strictly increasing sequence"""
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_all_equal_elements():
    """Test a sequence with all equal elements"""
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1

def test_empty_list():
    """Test an empty list"""
    assert longest_increasing_subsequence([]) == 0

def test_single_element():
    """Test a list with a single element"""
    assert longest_increasing_subsequence([42]) == 1

def test_decreasing_sequence():
    """Test a decreasing sequence"""
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_mixed_sequence():
    """Test a mixed sequence with multiple increasing subsequences"""
    assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_invalid_input_type():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")
    with pytest.raises(TypeError):
        longest_increasing_subsequence(42)

def test_non_integer_elements():
    """Test that non-integer elements raise ValueError"""
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, 3, "four", 5])
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1.5, 2.5, 3.5])