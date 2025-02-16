import pytest
from src.mode_finder import find_mode

def test_find_mode_single_mode():
    """Test finding a single mode in a list of numbers."""
    assert find_mode([1, 2, 2, 3, 4]) == 2
    assert find_mode([1.5, 2.5, 2.5, 3.5, 4.5]) == 2.5

def test_find_mode_multiple_modes():
    """Test finding multiple modes when they exist."""
    assert sorted(find_mode([1, 2, 2, 3, 3])) == [2, 3]
    assert sorted(find_mode([1.5, 2.5, 2.5, 3.5, 3.5])) == [2.5, 3.5]

def test_find_mode_all_unique():
    """Test when all numbers have the same frequency."""
    result = find_mode([1, 2, 3, 4, 5])
    assert result == 1  # Should return the first number when all have equal frequency

def test_find_mode_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find mode of an empty list"):
        find_mode([])

def test_find_mode_different_types():
    """Test mode with mixed integer and float types."""
    result = find_mode([1, 1.0, 2, 2.0, 3])
    assert any(x in result for x in [1, 2, 1.0, 2.0])  # Ensure mode contains one of these