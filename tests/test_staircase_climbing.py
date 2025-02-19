import pytest
from src.staircase_climbing import count_climbing_ways

def test_single_step_staircase():
    """Test a staircase with a single step of length 1"""
    assert count_climbing_ways([1]) == 1

def test_two_step_staircase():
    """Test a staircase with a two steps of length 1"""
    assert count_climbing_ways([1, 1]) == 2

def test_multiple_steps():
    """Test a staircase with multiple steps"""
    assert count_climbing_ways([1, 2, 1]) == 3

def test_large_staircase():
    """Test a larger staircase to verify complexity"""
    assert count_climbing_ways([1, 1, 1, 1]) == 5

def test_invalid_input_empty_list():
    """Test raising ValueError for empty list"""
    with pytest.raises(ValueError, match="Input must be a non-empty list of stair lengths"):
        count_climbing_ways([])

def test_invalid_input_negative_lengths():
    """Test raising ValueError for negative step lengths"""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_climbing_ways([-1, 2, 3])

def test_invalid_input_non_integer():
    """Test raising ValueError for non-integer step lengths"""
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_climbing_ways([1, 2, '3'])