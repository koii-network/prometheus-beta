import pytest
from src.fibonacci_utils import fibonacci, fibonacciSum

def test_fibonacci_sequence():
    assert fibonacci(1) == [1, 1]
    assert fibonacci(2) == [1, 1, 2]
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(0) == []
    assert fibonacci(100) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_fibonacci_sum():
    assert fibonacciSum([1]) == 2  # 1 + 1
    assert fibonacciSum([5]) == 20  # 1 + 1 + 2 + 3 + 5 + 8
    assert fibonacciSum([10]) == 42  # 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21
    assert fibonacciSum([1, 5, 10]) == 42  # max is 10
    assert fibonacciSum([100]) == 232  # sum of Fibonacci seq up to 100

def test_fibonacci_sum_error_cases():
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        fibonacciSum([])
    
    with pytest.raises(ValueError, match="All numbers in the array must be positive integers"):
        fibonacciSum([0])
    
    with pytest.raises(ValueError, match="All numbers in the array must be positive integers"):
        fibonacciSum([-1, 5, 10])