import pytest
from src.closest_pair import find_closest_pair

def test_basic_case():
    """Test a simple case with clear closest pair"""
    assert find_closest_pair([1, 3, 4, 7]) == (3, 4)

def test_negative_numbers():
    """Test case with negative numbers"""
    assert find_closest_pair([-1, -5, 3, 7]) == (-1, 3)

def test_duplicate_numbers():
    """Test case with duplicate numbers"""
    assert find_closest_pair([5, 5, 10, 15]) == (5, 5)

def test_multiple_pairs_with_same_difference():
    """Test when multiple pairs have the same difference"""
    assert find_closest_pair([1, 3, 4, 6]) == (1, 3)

def test_unsorted_input():
    """Test input that's not already sorted"""
    assert find_closest_pair([7, 2, 9, 5, 1]) == (1, 2)

def test_large_numbers():
    """Test case with large numbers"""
    assert find_closest_pair([1000, 2000, 1500, 1600]) == (1500, 1600)

def test_input_too_small():
    """Test that ValueError is raised for lists with fewer than 2 numbers"""
    with pytest.raises(ValueError, match="Input list must contain at least two numbers"):
        find_closest_pair([])

def test_input_single_element():
    """Test that ValueError is raised for a single-element list"""
    with pytest.raises(ValueError, match="Input list must contain at least two numbers"):
        find_closest_pair([42])