import pytest
from src.fibonacci_log_time import fibonacci_log_time

def test_fibonacci_basic_values():
    """Test basic known Fibonacci values."""
    assert fibonacci_log_time(0) == 0
    assert fibonacci_log_time(1) == 1
    assert fibonacci_log_time(2) == 1
    assert fibonacci_log_time(3) == 2
    assert fibonacci_log_time(4) == 3
    assert fibonacci_log_time(5) == 5
    assert fibonacci_log_time(6) == 8

def test_larger_fibonacci_numbers():
    """Test larger Fibonacci number calculations."""
    assert fibonacci_log_time(10) == 55
    assert fibonacci_log_time(20) == 6765
    assert fibonacci_log_time(30) == 832040

def test_very_large_fibonacci_numbers():
    """Test extremely large Fibonacci number calculations."""
    # These tests verify that the log(n) algorithm can handle large inputs efficiently
    assert fibonacci_log_time(50) == 12586269025
    assert fibonacci_log_time(70) == 190392490709135

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_time(-1)
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_time(-100)