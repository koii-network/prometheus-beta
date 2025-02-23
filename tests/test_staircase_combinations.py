import pytest
from src.staircase_combinations import calculate_staircase_combinations

def test_single_step_staircase():
    """Test a staircase with a single step"""
    assert calculate_staircase_combinations([1]) == 1

def test_two_step_staircase():
    """Test a staircase with two steps"""
    assert calculate_staircase_combinations([1, 1]) == 2

def test_multi_step_staircase():
    """Test a longer staircase"""
    assert calculate_staircase_combinations([1, 1, 1]) == 3

def test_different_step_lengths():
    """Test staircase with different step lengths"""
    assert calculate_staircase_combinations([2, 2]) == 2

def test_complex_staircase():
    """Test a more complex staircase scenario"""
    assert calculate_staircase_combinations([1, 2, 1]) == 3

def test_empty_staircase_raises_error():
    """Test that empty staircase raises ValueError"""
    with pytest.raises(ValueError, match="Stair lengths list cannot be empty"):
        calculate_staircase_combinations([])

def test_negative_step_length_raises_error():
    """Test that negative step lengths raise ValueError"""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        calculate_staircase_combinations([1, -1, 2])

def test_zero_step_length_raises_error():
    """Test that zero step lengths raise ValueError"""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        calculate_staircase_combinations([1, 0, 2])