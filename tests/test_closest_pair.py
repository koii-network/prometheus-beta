import pytest
from src.closest_pair import find_closest_pair

def test_basic_closest_pair():
    """Test finding the closest pair in a simple list."""
    assert find_closest_pair([1, 3, 4, 5]) == (3, 4)

def test_negative_numbers():
    """Test finding closest pair with negative numbers."""
    assert find_closest_pair([-1, -3, 4, 7, 5]) == (-1, -3)

def test_floating_point_numbers():
    """Test finding closest pair with floating point numbers."""
    assert find_closest_pair([1.1, 1.4, 2.5, 3.8]) == (1.1, 1.4)

def test_multiple_closest_pairs_with_smallest_numbers():
    """Test when multiple pairs have same difference, return smallest numbers."""
    assert find_closest_pair([1, 2, 3, 4, 5, 6]) == (1, 2)

def test_repeated_numbers():
    """Test with repeated numbers."""
    assert find_closest_pair([1, 1, 3, 4, 5]) == (1, 1)

def test_large_numbers():
    """Test with large numbers."""
    assert find_closest_pair([1000000, 1000001, 1000003, 1000005]) == (1000000, 1000001)

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError):
        find_closest_pair([])

def test_invalid_input_single_element():
    """Test that a single-element list raises a ValueError."""
    with pytest.raises(ValueError):
        find_closest_pair([42])

def test_unsorted_input():
    """Test that the function works with unsorted input."""
    assert find_closest_pair([5, 2, 3, 1, 4]) == (1, 2)