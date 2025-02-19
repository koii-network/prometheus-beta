import pytest
from src.closest_pair import find_closest_pair

def test_basic_find_closest_pair():
    """Test finding the closest pair in a simple list"""
    assert find_closest_pair([1, 3, 5, 7, 9]) == (1, 3)

def test_find_closest_pair_with_negatives():
    """Test finding closest pair with negative numbers"""
    assert find_closest_pair([-5, -2, 0, 2, 5]) == (-2, 0)

def test_find_closest_pair_with_duplicates():
    """Test finding closest pair when some numbers are the same"""
    assert find_closest_pair([1, 1, 2, 3, 4]) == (1, 1)

def test_find_closest_pair_random_order():
    """Test finding closest pair in an unsorted list"""
    assert find_closest_pair([7, 2, 9, 3, 1]) == (1, 2)

def test_find_closest_pair_tie_breaker():
    """Test that when multiple pairs have the same difference, 
    it returns the lexicographically smaller pair"""
    assert find_closest_pair([1, 4, 3, 8, 5]) == (3, 4)

def test_find_closest_pair_error_on_single_element():
    """Test that an error is raised when list has less than 2 elements"""
    with pytest.raises(ValueError, match="Input list must contain at least 2 numbers"):
        find_closest_pair([1])

def test_find_closest_pair_error_on_empty_list():
    """Test that an error is raised when list is empty"""
    with pytest.raises(ValueError, match="Input list must contain at least 2 numbers"):
        find_closest_pair([])