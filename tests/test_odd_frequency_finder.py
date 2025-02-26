import pytest
from src.odd_frequency_finder import find_odd_frequency_number

def test_basic_odd_frequency():
    """Test finding a number that appears an odd number of times."""
    assert find_odd_frequency_number([1, 1, 2, 2, 3]) == 3
    assert find_odd_frequency_number([1, 2, 3, 1, 2, 3, 3]) == 3

def test_multiple_odd_frequency_numbers():
    """Test returning the smallest number when multiple numbers appear odd times."""
    assert find_odd_frequency_number([1, 1, 2, 2, 3, 3, 3, 4, 4]) == 3

def test_single_number():
    """Test when there's only one number in the list."""
    assert find_odd_frequency_number([5]) == 5

def test_large_numbers():
    """Test with larger numbers."""
    assert find_odd_frequency_number([10, 10, 20, 20, 30]) == 30

def test_negative_numbers():
    """Test with negative numbers."""
    assert find_odd_frequency_number([-1, -1, 2, 2, 3]) == 3
    assert find_odd_frequency_number([-1, -1, -2, -2, -3]) == -3

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_odd_frequency_number([])

def test_no_odd_frequency_raises_error():
    """Test that a list with no number appearing odd times raises a ValueError."""
    with pytest.raises(ValueError, match="No number appears an odd number of times"):
        find_odd_frequency_number([1, 1, 2, 2, 3, 3])

def test_complex_scenario():
    """Test a more complex scenario with multiple numbers."""
    assert find_odd_frequency_number([1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 3