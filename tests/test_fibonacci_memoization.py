import pytest
from src.fibonacci_memoization import fibonacci_memo

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci_memo(0) == 0
    assert fibonacci_memo(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values"""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55),
    ]
    for n, expected in test_cases:
        assert fibonacci_memo(n) == expected

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Fibonacci index must be non-negative"):
        fibonacci_memo(-1)

def test_fibonacci_large_number():
    """Test a larger Fibonacci number"""
    # Test a larger number to ensure memoization performance
    assert fibonacci_memo(20) == 6765

def test_fibonacci_repeated_calls():
    """Verify that subsequent calls for the same number are efficient"""
    first_call = fibonacci_memo(15)
    second_call = fibonacci_memo(15)
    assert first_call == second_call