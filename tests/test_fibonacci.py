import pytest
from src.fibonacci import fibonacci_memoized

def test_fibonacci_basic_cases():
    # Test base cases and first few Fibonacci numbers
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1
    assert fibonacci_memoized(2) == 1
    assert fibonacci_memoized(3) == 2
    assert fibonacci_memoized(4) == 3
    assert fibonacci_memoized(5) == 5
    assert fibonacci_memoized(6) == 8

def test_fibonacci_larger_numbers():
    # Test larger Fibonacci numbers
    assert fibonacci_memoized(10) == 55
    assert fibonacci_memoized(15) == 610
    assert fibonacci_memoized(20) == 6765

def test_invalid_input():
    # Test negative input
    with pytest.raises(ValueError):
        fibonacci_memoized(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError):
        fibonacci_memoized(3.5)
    with pytest.raises(TypeError):
        fibonacci_memoized("5")

def test_memoization_efficiency():
    # Demonstrate memoization by checking repeated calls
    first_call = fibonacci_memoized(100)  # Large number to show efficiency
    second_call = fibonacci_memoized(100)  # Should be very fast due to memoization
    assert first_call == second_call