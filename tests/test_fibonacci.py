import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (10, 55)
    ]
    for n, expected in test_cases:
        assert fibonacci(n) == expected

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers."""
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040

def test_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)

def test_fibonacci_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(None)