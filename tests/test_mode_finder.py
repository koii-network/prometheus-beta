import pytest
from mode_finder import find_mode

def test_single_mode():
    """Test a list with a single mode"""
    assert find_mode([1, 2, 2, 3, 4]) == 2

def test_multiple_modes():
    """Test a list with multiple modes"""
    assert set(find_mode([1, 2, 2, 3, 3, 4])) == {2, 3}

def test_all_unique_numbers():
    """Test a list where all numbers appear once"""
    result = find_mode([1, 2, 3, 4, 5])
    assert result in [1, 2, 3, 4, 5]

def test_floating_point_numbers():
    """Test mode with floating point numbers"""
    result = find_mode([1.5, 2.3, 1.5, 2.3, 3.7])
    assert set(result) == {1.5, 2.3}

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find mode of an empty list"):
        find_mode([])