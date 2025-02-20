import pytest
from src.find_odd_occurrence import find_odd_occurrence

def test_basic_odd_occurrence():
    # Simple case with one number appearing odd times
    assert find_odd_occurrence([1, 1, 2, 2, 3]) == 3

def test_smallest_odd_occurrence():
    # Multiple numbers with odd occurrences, return smallest
    assert find_odd_occurrence([1, 1, 2, 2, 3, 3, 3]) == 3

def test_single_number():
    # Single number in the list
    assert find_odd_occurrence([5]) == 5

def test_large_numbers():
    # Test with larger numbers
    assert find_odd_occurrence([10, 20, 10, 20, 30, 30, 30]) == 30

def test_negative_numbers():
    # Test with negative numbers
    assert find_odd_occurrence([-1, -1, 2, 2, -3]) == -3

def test_empty_list_raises_error():
    # Empty list should raise a ValueError
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_occurrence([])

def test_no_odd_occurrence_raises_error():
    # List with all even occurrences should raise a ValueError
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_occurrence([1, 1, 2, 2, 3, 3])