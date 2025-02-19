import pytest
from src.fibonacci_utils import fibonacci, fibonacciSum

def test_fibonacci():
    # Test Fibonacci generation
    assert fibonacci(0) == [0]
    assert fibonacci(1) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(-1) == []

def test_fibonacci_sum():
    # Test FibonacciSum with various inputs
    assert fibonacciSum([5]) == 12  # 0 + 1 + 1 + 2 + 3 + 5
    assert fibonacciSum([1, 2, 3]) == 7  # 0 + 1 + 1 + 2 + 3
    assert fibonacciSum([10]) == 27  # 0 + 1 + 1 + 2 + 3 + 5 + 8
    assert fibonacciSum([100]) == 88  # 0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34

def test_fibonacci_sum_edge_cases():
    # Test edge cases
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        fibonacciSum([])
    
    with pytest.raises(ValueError, match="All numbers in the array must be positive integers"):
        fibonacciSum([0])
    
    with pytest.raises(ValueError, match="All numbers in the array must be positive integers"):
        fibonacciSum([-1, 2, 3])
    
    with pytest.raises(ValueError, match="All numbers in the array must be positive integers"):
        fibonacciSum([1, -2, 3])