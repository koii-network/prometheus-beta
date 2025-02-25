import pytest
from src.find_missing_numbers import find_missing_numbers

def test_basic_missing_numbers():
    """Test finding missing numbers in a typical scenario."""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_no_missing_numbers():
    """Test when there are no missing numbers in the array."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_single_element_array():
    """Test with a single element array."""
    assert find_missing_numbers([5]) == []

def test_consecutive_numbers():
    """Test with consecutive numbers."""
    assert find_missing_numbers([10, 12, 14, 16]) == [11, 13, 15]

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])

def test_none_input_raises_error():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be None"):
        find_missing_numbers(None)

def test_non_integer_input_raises_error():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        find_missing_numbers([1, 2, 'a', 4])

def test_large_range_of_missing_numbers():
    """Test finding missing numbers in a larger range."""
    assert find_missing_numbers([1, 10]) == list(range(2, 10))

def test_negative_numbers():
    """Test finding missing numbers with negative numbers."""
    assert find_missing_numbers([-5, -2]) == [-4, -3]