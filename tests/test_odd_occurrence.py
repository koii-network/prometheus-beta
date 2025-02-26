import pytest
from src.odd_occurrence import find_odd_occurrence

def test_basic_odd_occurrence():
    """Test finding a number that appears an odd number of times"""
    assert find_odd_occurrence([1, 1, 2, 2, 3]) == 3

def test_multiple_odd_occurrences():
    """Test returning the smallest number when multiple numbers appear odd times"""
    assert find_odd_occurrence([1, 1, 2, 2, 3, 3, 3, 4, 4]) == 3

def test_single_number():
    """Test with a single number"""
    assert find_odd_occurrence([5]) == 5

def test_large_numbers():
    """Test with larger numbers"""
    assert find_odd_occurrence([10, 10, 20, 20, 30]) == 30

def test_negative_numbers():
    """Test with negative numbers"""
    assert find_odd_occurrence([-1, -1, 2, 2, -3]) == -3

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_occurrence([])

def test_no_odd_occurrence_raises_error():
    """Test that no odd occurrence raises a ValueError"""
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_occurrence([1, 1, 2, 2, 3, 3])