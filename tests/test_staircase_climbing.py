import pytest
from src.staircase_climbing import climb_stairs

def test_climb_stairs_base_cases():
    """Test the base cases of the staircase climbing function."""
    assert climb_stairs(0) == 1  # No steps
    assert climb_stairs(1) == 1  # One step

def test_climb_stairs_known_cases():
    """Test known staircase climbing scenarios."""
    assert climb_stairs(2) == 2   # (1+1, 2)
    assert climb_stairs(3) == 3   # (1+1+1, 1+2, 2+1)
    assert climb_stairs(4) == 5   # (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)
    assert climb_stairs(5) == 8   # Multiple combinations

def test_climb_stairs_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of steps cannot be negative"):
        climb_stairs(-1)

def test_climb_stairs_large_input():
    """Test the function with a larger input to ensure it handles bigger staircases."""
    assert climb_stairs(10) == 89  # Verified from known Fibonacci-like sequence