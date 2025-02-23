import pytest
from src.fibonacci_utils import fibonacci, fibonacci_sum

def test_fibonacci_basic_sequence():
    """Test basic Fibonacci sequence generation"""
    assert fibonacci(1) == [1, 1]
    assert fibonacci(2) == [1, 1]
    assert fibonacci(3) == [1, 1, 2]
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8]
    assert fibonacci(0) == []

def test_fibonacci_edge_cases():
    """Test edge cases for fibonacci"""
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_sum_basic():
    """Test basic Fibonacci sum functionality"""
    assert fibonacci_sum([1]) == 2  # 1 + 1
    assert fibonacci_sum([2]) == 4  # 1 + 1 + 2
    assert fibonacci_sum([3]) == 7  # 1 + 1 + 2 + 3
    assert fibonacci_sum([10]) == 20  # 1 + 1 + 2 + 3 + 5 + 8

def test_fibonacci_sum_multiple_numbers():
    """Test Fibonacci sum with multiple input numbers"""
    assert fibonacci_sum([2, 5, 10]) == 20  # Same as previous test
    assert fibonacci_sum([1, 3, 7]) == 16  # 1 + 1 + 2 + 3 + 5

def test_fibonacci_sum_edge_cases():
    """Test edge cases for fibonacci_sum"""
    assert fibonacci_sum([]) == 0
    
    with pytest.raises(ValueError):
        fibonacci_sum(None)
    
    with pytest.raises(ValueError):
        fibonacci_sum([-1, 2, 3])
    
    with pytest.raises(ValueError):
        fibonacci_sum([1.5, 2, 3])

def test_fibonacci_sum_large_numbers():
    """Test Fibonacci sum with larger numbers"""
    result = fibonacci_sum([100])
    assert result > 0
    
    result_multiple = fibonacci_sum([50, 100, 200])
    assert result_multiple > 0