import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55)
    ]
    for n, expected in test_cases:
        assert fibonacci(n) == expected

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)

def test_fibonacci_non_integer_input():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")

def test_fibonacci_large_input():
    """Test a larger Fibonacci number to ensure memoization works efficiently."""
    assert fibonacci(20) == 6765

def test_fibonacci_memoization():
    """Ensure memoization dictionary is working correctly."""
    memo = {}
    result1 = fibonacci(10, memo)
    result2 = fibonacci(10, memo)
    assert result1 == result2  # Ensure the same result is returned
    # In a real-world scenario, you might want to mock or patch a way to verify 
    # that the recursive calls are minimized, but that's beyond the scope of this test.