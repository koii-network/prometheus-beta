import pytest
from src.fibonacci_log_n import fibonacci_log_n

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci sequence"""
    assert fibonacci_log_n(0) == 0
    assert fibonacci_log_n(1) == 1
    assert fibonacci_log_n(2) == 1

def test_fibonacci_sequence():
    """Test several known Fibonacci numbers"""
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for i, expected in enumerate(expected_sequence):
        assert fibonacci_log_n(i) == expected

def test_larger_fibonacci_numbers():
    """Test larger Fibonacci numbers"""
    assert fibonacci_log_n(10) == 55
    assert fibonacci_log_n(20) == 6765
    assert fibonacci_log_n(30) == 832040

def test_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_n(-1)

def test_type_input():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError):
        fibonacci_log_n(3.14)
    with pytest.raises(TypeError):
        fibonacci_log_n("5")