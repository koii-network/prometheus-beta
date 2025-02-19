import pytest
from src.fibonacci import fibonacci_generator

def test_fibonacci_generator_zero():
    """Test generating 0 Fibonacci numbers"""
    assert fibonacci_generator(0) == []

def test_fibonacci_generator_one():
    """Test generating 1 Fibonacci number"""
    assert fibonacci_generator(1) == [0]

def test_fibonacci_generator_two():
    """Test generating 2 Fibonacci numbers"""
    assert fibonacci_generator(2) == [0, 1]

def test_fibonacci_generator_multiple():
    """Test generating multiple Fibonacci numbers"""
    assert fibonacci_generator(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_generator_large():
    """Test generating a larger set of Fibonacci numbers"""
    result = fibonacci_generator(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_generator_negative():
    """Test that generating negative Fibonacci numbers raises a ValueError"""
    with pytest.raises(ValueError, match="Number of Fibonacci numbers must be non-negative"):
        fibonacci_generator(-1)