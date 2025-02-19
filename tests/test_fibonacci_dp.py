import pytest
from src.fibonacci_dp import fibonacci_dynamic_programming

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci_dynamic_programming(0) == 0
    assert fibonacci_dynamic_programming(1) == 1

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
        assert fibonacci_dynamic_programming(n) == expected

def test_fibonacci_large_number():
    """Test a larger Fibonacci number to check efficiency."""
    assert fibonacci_dynamic_programming(20) == 6765

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        fibonacci_dynamic_programming("5")
    
    with pytest.raises(TypeError):
        fibonacci_dynamic_programming(5.5)
    
    with pytest.raises(ValueError):
        fibonacci_dynamic_programming(-1)
    
    with pytest.raises(ValueError):
        fibonacci_dynamic_programming(-100)