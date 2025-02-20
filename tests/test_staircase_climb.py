import pytest
from src.staircase_climb import climb_stairs

def test_zero_steps():
    """Test climbing 0 steps"""
    assert climb_stairs(0) == 1

def test_one_step():
    """Test climbing 1 step"""
    assert climb_stairs(1) == 1

def test_two_steps():
    """Test climbing 2 steps"""
    assert climb_stairs(2) == 2

def test_five_steps():
    """Test climbing 5 steps"""
    assert climb_stairs(5) == 8

def test_ten_steps():
    """Test climbing 10 steps"""
    assert climb_stairs(10) == 89

def test_negative_steps():
    """Test that negative steps raise a ValueError"""
    with pytest.raises(ValueError, match="Number of steps must be non-negative"):
        climb_stairs(-1)