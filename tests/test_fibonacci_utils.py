import pytest
from src.fibonacci_utils import fibonacci, fibonacciSum

def test_fibonacci():
    # Test generating Fibonacci sequence for different inputs
    assert fibonacci(0) == []
    assert fibonacci(1) == [1, 1]
    assert fibonacci(2) == [1, 1, 2]
    assert fibonacci(5) == [1, 1, 2, 3, 5]
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(20) == [1, 1, 2, 3, 5, 8, 13]
    assert fibonacci(-1) == []

def test_fibonacciSum():
    # Test sum of Fibonacci sequence for different input arrays
    assert fibonacciSum([1]) == 2  # [1, 1]
    assert fibonacciSum([2]) == 4  # [1, 1, 2]
    assert fibonacciSum([5]) == 12  # [1, 1, 2, 3, 5]
    assert fibonacciSum([10]) == 20  # [1, 1, 2, 3, 5, 8]
    assert fibonacciSum([1, 2, 3]) == 7  # Based on max(1,2,3) which is 3
    assert fibonacciSum([20]) == 33  # [1, 1, 2, 3, 5, 8, 13]

def test_fibonacciSum_error_handling():
    # Test error handling for invalid inputs
    with pytest.raises(ValueError):
        fibonacciSum([])
    with pytest.raises(ValueError):
        fibonacciSum([-1, 2, 3])
    with pytest.raises(ValueError):
        fibonacciSum([1.5, 2, 3])
    with pytest.raises(ValueError):
        fibonacciSum(['a', 'b', 'c'])