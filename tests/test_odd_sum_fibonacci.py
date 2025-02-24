import pytest
from src.odd_sum_fibonacci import generate_odd_sum_fibonacci

def test_generate_odd_sum_fibonacci_basic():
    """Test basic functionality of the function."""
    sequence = generate_odd_sum_fibonacci(5)
    assert len(sequence) == 5
    assert sequence == [0, 1, 1, 2, 3]

def test_generate_odd_sum_fibonacci_zero():
    """Test generating 0 elements."""
    assert generate_odd_sum_fibonacci(0) == []

def test_generate_odd_sum_fibonacci_one():
    """Test generating 1 element."""
    assert generate_odd_sum_fibonacci(1) == [0]

def test_generate_odd_sum_fibonacci_two():
    """Test generating 2 elements."""
    assert generate_odd_sum_fibonacci(2) == [0, 1]

def test_generate_odd_sum_fibonacci_type_input():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci("5")
        generate_odd_sum_fibonacci(5.5)
        generate_odd_sum_fibonacci(None)

def test_generate_odd_sum_fibonacci_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of elements must be non-negative"):
        generate_odd_sum_fibonacci(-1)

def test_generate_odd_sum_fibonacci_longer_sequence():
    """Test a longer sequence generation."""
    sequence = generate_odd_sum_fibonacci(10)
    assert len(sequence) == 10
    assert sequence == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_generate_odd_sum_fibonacci_very_long_sequence():
    """Test generating a very long sequence."""
    sequence = generate_odd_sum_fibonacci(15)
    assert len(sequence) == 15