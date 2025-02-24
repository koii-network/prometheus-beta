import pytest
from src.find_non_duplicate import find_single_non_duplicate

def test_single_non_duplicate_middle():
    """Test finding non-duplicate element in the middle of the array."""
    assert find_single_non_duplicate([1, 1, 2, 3, 3, 4, 4]) == 2

def test_single_non_duplicate_start():
    """Test finding non-duplicate element at the start of the array."""
    assert find_single_non_duplicate([2, 3, 3, 4, 4, 5, 5]) == 2

def test_single_non_duplicate_end():
    """Test finding non-duplicate element at the end of the array."""
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 4, 4]) == 3

def test_single_element_array():
    """Test array with only one element."""
    assert find_single_non_duplicate([5]) == 5

def test_two_unique_elements():
    """Test array with two different unique elements."""
    assert find_single_non_duplicate([1, 1, 2, 2, 3, 4, 4]) == 3

def test_empty_array_raises_error():
    """Test that empty array raises ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_single_non_duplicate([])

def test_no_unique_element_raises_error():
    """Test that an array without a unique element raises ValueError."""
    with pytest.raises(ValueError, match="No single non-duplicate element found"):
        find_single_non_duplicate([1, 1, 2, 2])

def test_large_array():
    """Test with a larger array to ensure performance."""
    large_arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9]
    assert find_single_non_duplicate(large_arr) == 6