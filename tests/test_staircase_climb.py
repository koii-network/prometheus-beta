import pytest
from src.staircase_climb import calculate_climb_combinations

def test_single_stair():
    """Test climbing a single stair of length 1."""
    assert calculate_climb_combinations([1]) == 1

def test_two_stairs():
    """Test climbing two stairs of length 1."""
    assert calculate_climb_combinations([1, 1]) == 2

def test_multiple_stairs():
    """Test climbing multiple stairs."""
    assert calculate_climb_combinations([1, 2, 3]) == 3

def test_different_stair_lengths():
    """Test climbing stairs with different lengths."""
    assert calculate_climb_combinations([3, 2, 1]) == 3

def test_large_staircase():
    """Test a larger staircase."""
    assert calculate_climb_combinations([1, 1, 1, 1, 1]) == 8

def test_empty_staircase():
    """Test that an empty staircase raises a ValueError."""
    with pytest.raises(ValueError, match="Stair lengths list cannot be empty"):
        calculate_climb_combinations([])

def test_negative_stairs():
    """Test that negative stair lengths raise a ValueError."""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        calculate_climb_combinations([1, -2, 3])

def test_zero_stairs():
    """Test that zero stair lengths raise a ValueError."""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        calculate_climb_combinations([1, 0, 3])