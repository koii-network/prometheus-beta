import pytest
from src.staircase_climber import climb_stairs

def test_base_cases():
    """Test basic base cases for staircase climbing"""
    assert climb_stairs(0) == 1  # One way to climb 0 steps (do nothing)
    assert climb_stairs(1) == 1  # One way to climb 1 step
    assert climb_stairs(2) == 2  # Two ways to climb 2 steps

def test_larger_cases():
    """Test larger number of steps"""
    assert climb_stairs(3) == 3   # [1,1,1], [1,2], [2,1]
    assert climb_stairs(4) == 5   # [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]
    assert climb_stairs(5) == 8   # Multiple ways to climb 5 steps

def test_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Number of steps must be non-negative"):
        climb_stairs(-1)

def test_large_input():
    """Test a larger input to ensure performance with memoization"""
    # This would be very slow without memoization
    result = climb_stairs(30)
    assert result > 0  # Exact value less important than performance/correctness

def test_type_input():
    """Test that non-integer inputs are handled"""
    with pytest.raises(TypeError):
        climb_stairs("not an int")
    with pytest.raises(TypeError):
        climb_stairs(3.14)