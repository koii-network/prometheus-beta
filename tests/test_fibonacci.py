import pytest
from src.fibonacci import memoized_fibonacci

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert memoized_fibonacci(0) == 0
    assert memoized_fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    assert memoized_fibonacci(2) == 1
    assert memoized_fibonacci(3) == 2
    assert memoized_fibonacci(4) == 3
    assert memoized_fibonacci(5) == 5
    assert memoized_fibonacci(6) == 8
    assert memoized_fibonacci(10) == 55

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers to verify memoization efficiency."""
    assert memoized_fibonacci(20) == 6765
    assert memoized_fibonacci(30) == 832040

def test_fibonacci_negative_input():
    """Test handling of negative input."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        memoized_fibonacci(-1)

def test_fibonacci_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        memoized_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        memoized_fibonacci("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        memoized_fibonacci(None)