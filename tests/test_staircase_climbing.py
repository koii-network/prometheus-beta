import pytest
from src.staircase_climbing import calculate_climbing_ways

def test_single_step_staircase():
    """Test a staircase with a single step of length 1"""
    assert calculate_climbing_ways([1]) == 1

def test_two_step_staircase():
    """Test a staircase with two steps of length 1"""
    assert calculate_climbing_ways([1, 1]) == 2

def test_three_step_staircase():
    """Test a staircase with three steps of length 1"""
    assert calculate_climbing_ways([1, 1, 1]) == 3

def test_different_step_lengths():
    """Test a staircase with different step lengths"""
    assert calculate_climbing_ways([2, 1, 2]) == 3

def test_empty_staircase():
    """Test that an empty staircase raises a ValueError"""
    with pytest.raises(ValueError, match="Stair lengths cannot be empty"):
        calculate_climbing_ways([])

def test_negative_step_lengths():
    """Test that negative or zero step lengths raise a ValueError"""
    with pytest.raises(ValueError, match="All stair lengths must be positive"):
        calculate_climbing_ways([1, -2, 3])
    
    with pytest.raises(ValueError, match="All stair lengths must be positive"):
        calculate_climbing_ways([0, 1, 2])

def test_large_staircase():
    """Test a larger staircase to verify computational correctness"""
    assert calculate_climbing_ways([1] * 10) == 89