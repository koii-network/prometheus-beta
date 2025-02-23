import pytest
from src.mode_finder import find_mode

def test_single_mode():
    """Test finding a single mode in a list of numbers."""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test finding multiple modes when frequencies are equal."""
    assert sorted(find_mode([1, 2, 2, 3, 3, 4])) == [2, 3]

def test_all_unique_numbers():
    """Test case where all numbers appear once."""
    assert find_mode([1, 2, 3, 4, 5]) in [1, 2, 3, 4, 5]

def test_single_number():
    """Test list with a single number."""
    assert find_mode([42]) == 42

def test_float_numbers():
    """Test mode with floating point numbers."""
    assert find_mode([1.5, 2.5, 2.5, 3.5]) == 2.5

def test_mixed_types():
    """Test mode with mixed integer and float types."""
    assert find_mode([1, 2.0, 2, 3.0, 2.0]) == 2

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find mode of an empty list"):
        find_mode([])