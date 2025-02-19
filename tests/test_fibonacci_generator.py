import pytest
from src.fibonacci_generator import fibonacci_generator

def test_fibonacci_generator_zero():
    """Test generating 0 Fibonacci numbers."""
    assert fibonacci_generator(0) == []

def test_fibonacci_generator_one():
    """Test generating 1 Fibonacci number."""
    assert fibonacci_generator(1) == [0]

def test_fibonacci_generator_two():
    """Test generating 2 Fibonacci numbers."""
    assert fibonacci_generator(2) == [0, 1]

def test_fibonacci_generator_five():
    """Test generating 5 Fibonacci numbers."""
    assert fibonacci_generator(5) == [0, 1, 1, 2, 3]

def test_fibonacci_generator_ten():
    """Test generating 10 Fibonacci numbers."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci_generator(10) == expected

def test_fibonacci_generator_negative():
    """Test that generating negative Fibonacci numbers raises a ValueError."""
    with pytest.raises(ValueError, match="Number of Fibonacci numbers must be non-negative"):
        fibonacci_generator(-1)