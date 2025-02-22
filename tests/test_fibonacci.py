import pytest
from src.fibonacci import fibonacci_log_n

def test_fibonacci_log_n_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci_log_n(0) == 0
    assert fibonacci_log_n(1) == 1

def test_fibonacci_log_n_known_values():
    """Test known Fibonacci sequence values"""
    expected_values = [
        (2, 1),   # F(2) = 1
        (3, 2),   # F(3) = 2
        (4, 3),   # F(4) = 3
        (5, 5),   # F(5) = 5
        (6, 8),   # F(6) = 8
        (10, 55), # F(10) = 55
        (20, 6765) # F(20) = 6765
    ]
    
    for n, expected in expected_values:
        assert fibonacci_log_n(n) == expected

def test_fibonacci_log_n_larger_numbers():
    """Test larger Fibonacci numbers"""
    assert fibonacci_log_n(30) == 832040
    assert fibonacci_log_n(40) == 102334155

def test_fibonacci_log_n_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_n(-1)
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_n(-100)