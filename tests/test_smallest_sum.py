import pytest
from src.smallest_sum import find_smallest_sum

def test_basic_scenario():
    """Test basic scenario with simple lists"""
    assert find_smallest_sum([1, 2, 3], [4, 5, 6]) == 5

def test_negative_numbers():
    """Test scenario with negative numbers"""
    assert find_smallest_sum([-1, -2], [-3, -4]) == -7

def test_mixed_numbers():
    """Test scenario with mixed positive and negative numbers"""
    assert find_smallest_sum([-1, 2], [3, -4]) == -5

def test_empty_list():
    """Test scenario where one list is empty"""
    assert find_smallest_sum([], [1, 2, 3]) == 0
    assert find_smallest_sum([1, 2, 3], []) == 0

def test_single_element_lists():
    """Test scenario with single-element lists"""
    assert find_smallest_sum([1], [2]) == 3

def test_invalid_input_non_list():
    """Test that function raises error for non-list inputs"""
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_sum(1, [2])

def test_invalid_input_non_integer():
    """Test that function raises error for non-integer elements"""
    with pytest.raises(ValueError, match="All list elements must be integers"):
        find_smallest_sum([1, 'a'], [2, 3])

def test_lists_of_different_lengths():
    """Test scenario with lists of different lengths"""
    assert find_smallest_sum([1, 2], [3, 4, 5]) == 4