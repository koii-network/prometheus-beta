import pytest
from src.fibonacci import fibonacci_recursive

def test_fibonacci_base_cases():
    """Test base cases of the Fibonacci sequence."""
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13)
    ]
    for n, expected in test_cases:
        assert fibonacci_recursive(n) == expected

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_recursive(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_recursive("5")
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_recursive(-1)

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers to check recursive correctness."""
    # Note: This is a bit slow due to recursive implementation
    assert fibonacci_recursive(10) == 55
    assert fibonacci_recursive(15) == 610