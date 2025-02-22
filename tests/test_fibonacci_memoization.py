import pytest
from src.fibonacci_memoization import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers"""
    expected_values = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55)
    ]
    
    for n, expected in expected_values:
        assert fibonacci_memoized(n) == expected, f"Failed for n={n}"

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers"""
    # These are computationally intensive, checking they can be computed
    assert fibonacci_memoized(20) == 6765
    assert fibonacci_memoized(30) == 832040

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_memoized(-1)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        fibonacci_memoized(3.14)
    
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        fibonacci_memoized("5")