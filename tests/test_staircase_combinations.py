import pytest
from src.staircase_combinations import calculate_staircase_combinations

def test_basic_single_length_staircase():
    """Test a basic staircase with a single step length."""
    assert calculate_staircase_combinations([3]) == 3

def test_multiple_step_lengths():
    """Test a staircase with multiple step lengths."""
    assert calculate_staircase_combinations([1, 2]) == 5

def test_complex_staircase():
    """Test a more complex staircase configuration."""
    assert calculate_staircase_combinations([2, 3, 1]) == 13

def test_empty_staircase():
    """Test an empty staircase returns 1 (base case)."""
    assert calculate_staircase_combinations([]) == 1

def test_invalid_input_non_list():
    """Test that non-list input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a list of integers"):
        calculate_staircase_combinations("invalid")

def test_invalid_input_negative_lengths():
    """Test that negative or non-integer lengths raise a ValueError."""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        calculate_staircase_combinations([1, -2, 3])
    
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        calculate_staircase_combinations([1, 2.5, 3])

def test_large_staircase():
    """Test a larger staircase to check performance and correctness."""
    assert calculate_staircase_combinations([1, 2, 3, 4]) == 81