import pytest
from src.fibonacci_utils import fibonacci, fibonacci_sum

def test_fibonacci_basic():
    """Test basic Fibonacci sequence generation"""
    assert fibonacci(0) == [0]
    assert fibonacci(1) == [0, 1]
    assert fibonacci(2) == [0, 1, 1, 2]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
    assert fibonacci(20) == [0, 1, 1, 2, 3, 5, 8, 13]

def test_fibonacci_invalid_input():
    """Test invalid inputs for Fibonacci function"""
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci("not a number")

def test_fibonacci_sum_basic():
    """Test basic Fibonacci sum functionality"""
    assert fibonacci_sum([0]) == 0
    assert fibonacci_sum([1]) == 1
    assert fibonacci_sum([2]) == 4  # 0 + 1 + 1 + 2
    assert fibonacci_sum([5]) == 12  # 0 + 1 + 1 + 2 + 3 + 5
    assert fibonacci_sum([10]) == 20  # 0 + 1 + 1 + 2 + 3 + 5 + 8

def test_fibonacci_sum_multiple_inputs():
    """Test Fibonacci sum with multiple inputs"""
    assert fibonacci_sum([1, 3, 5]) == 12  # uses max as 5
    assert fibonacci_sum([2, 7, 10]) == 20  # uses max as 10

def test_fibonacci_sum_edge_cases():
    """Test edge cases for Fibonacci sum"""
    assert fibonacci_sum([]) == 0
    assert fibonacci_sum([0]) == 0

def test_fibonacci_sum_invalid_input():
    """Test invalid inputs for Fibonacci sum"""
    with pytest.raises(ValueError):
        fibonacci_sum([-1, 2, 3])
    with pytest.raises(ValueError):
        fibonacci_sum(["not", "a", "number"])
    with pytest.raises(ValueError):
        fibonacci_sum([1.5, 2, 3])