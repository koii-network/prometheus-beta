import pytest
from src.staircase_climbing import climb_stairs

def test_climb_stairs_base_cases():
    # Test base cases
    assert climb_stairs(0) == 1  # No steps
    assert climb_stairs(1) == 1  # One step
    assert climb_stairs(2) == 2  # Can go 1+1 or 2 steps

def test_climb_stairs_larger_numbers():
    # Test larger numbers 
    assert climb_stairs(3) == 3   # [1,1,1], [1,2], [2,1]
    assert climb_stairs(4) == 5   # [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]
    assert climb_stairs(5) == 8   # Increasing complexity case

def test_climb_stairs_invalid_input():
    # Test negative input
    with pytest.raises(ValueError, match="Number of steps cannot be negative"):
        climb_stairs(-1)

def test_climb_stairs_performance():
    # Ensure function can handle larger inputs efficiently
    # These numbers would cause stack overflow with naive recursive approach
    result_10 = climb_stairs(10)
    result_20 = climb_stairs(20)
    
    assert result_10 == 89
    assert result_20 == 10946