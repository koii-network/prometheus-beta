import pytest
from src.fibonacci_utils import fibonacci, fibonacci_sum

def test_fibonacci_basic():
    """Test basic Fibonacci sequence generation"""
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(1) == [1]
    assert fibonacci(0) == []

def test_fibonacci_edge_cases():
    """Test edge cases for Fibonacci sequence generation"""
    assert fibonacci(2) == [1, 1, 2]
    assert fibonacci(7) == [1, 1, 2, 3, 5]

def test_fibonacci_negative_input():
    """Test handling of negative input"""
    with pytest.raises(ValueError, match="Maximum number must be non-negative"):
        fibonacci(-1)

def test_fibonacci_sum_basic():
    """Test basic Fibonacci sum calculation"""
    assert fibonacci_sum([5]) == 7  # 1 + 1 + 2 + 3
    assert fibonacci_sum([10]) == 20  # 1 + 1 + 2 + 3 + 5 + 8
    assert fibonacci_sum([1, 2, 3]) == 7  # 1 + 1 + 2 + 3

def test_fibonacci_sum_multiple_inputs():
    """Test Fibonacci sum with multiple input values"""
    assert fibonacci_sum([5, 7, 10]) == 20  # max is 10
    assert fibonacci_sum([1, 2, 3, 4, 5]) == 7  # max is 5

def test_fibonacci_sum_edge_cases():
    """Test edge cases for Fibonacci sum"""
    assert fibonacci_sum([1]) == 1
    assert fibonacci_sum([2]) == 2

def test_fibonacci_sum_error_cases():
    """Test error handling for Fibonacci sum"""
    # Empty array
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        fibonacci_sum([])
    
    # Non-positive numbers
    with pytest.raises(ValueError, match="All numbers in the array must be positive"):
        fibonacci_sum([0])
    
    with pytest.raises(ValueError, match="All numbers in the array must be positive"):
        fibonacci_sum([-1, 2, 3])