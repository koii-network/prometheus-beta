import pytest
from src.closest_pair import find_closest_pair

def test_basic_find_closest_pair():
    """Test finding the closest pair in a simple list."""
    assert find_closest_pair([1, 3, 5, 7, 9]) == (1, 3)

def test_find_closest_pair_with_negative_numbers():
    """Test finding closest pair with negative numbers."""
    assert find_closest_pair([-5, -2, 0, 3, 7]) == (-2, 0)

def test_find_closest_pair_with_decimals():
    """Test finding closest pair with decimal numbers."""
    assert find_closest_pair([1.1, 1.5, 3.2, 4.7]) == (1.1, 1.5)

def test_find_closest_pair_with_duplicates():
    """Test that function works with duplicate numbers."""
    assert find_closest_pair([5, 5, 5, 5]) == (5, 5)

def test_find_closest_pair_with_tie_returns_smallest_numbers():
    """Test that when multiple pairs have same difference, 
    the pair with smallest numbers is returned."""
    assert find_closest_pair([1, 4, 5, 8, 9]) == (4, 5)

def test_raise_error_with_insufficient_numbers():
    """Test that an error is raised when fewer than 2 numbers are provided."""
    with pytest.raises(ValueError, match="Input list must contain at least 2 numbers"):
        find_closest_pair([1])

def test_raise_error_with_empty_list():
    """Test that an error is raised with an empty list."""
    with pytest.raises(ValueError, match="Input list must contain at least 2 numbers"):
        find_closest_pair([])