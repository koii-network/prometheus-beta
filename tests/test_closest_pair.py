import pytest
from src.closest_pair import find_closest_pair

def test_basic_case():
    """Test finding closest pair in a simple list."""
    assert find_closest_pair([1, 3, 5, 7, 9]) == (1, 3)

def test_duplicate_numbers():
    """Test list with duplicate numbers."""
    assert find_closest_pair([1, 1, 3, 5, 7]) == (1, 1)

def test_negative_numbers():
    """Test list with negative numbers."""
    assert find_closest_pair([-5, -2, 0, 3, 7]) == (-5, -2)

def test_mixed_numbers():
    """Test list with mixed positive and negative numbers."""
    assert find_closest_pair([-10, 5, 2, -3, 7, 8]) == (-3, 2)

def test_very_close_pair():
    """Test list with a pair very close together."""
    assert find_closest_pair([1, 1.0001, 5, 10]) == (1, 1.0001)

def test_error_empty_list():
    """Test error handling for empty list."""
    with pytest.raises(ValueError, match="Input list must contain at least two numbers"):
        find_closest_pair([])

def test_error_single_element():
    """Test error handling for single-element list."""
    with pytest.raises(ValueError, match="Input list must contain at least two numbers"):
        find_closest_pair([42])

def test_single_pair():
    """Test a list with exactly two numbers."""
    assert find_closest_pair([5, 10]) == (5, 10)

def test_large_range():
    """Test a list with a large range of numbers."""
    nums = [1000, 2000, 1, 3000, 500, 750, 1500]
    assert find_closest_pair(nums) == (500, 750)