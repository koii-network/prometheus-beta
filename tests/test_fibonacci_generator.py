import pytest
from src.fibonacci_generator import fibonacci_generator

def test_fibonacci_generator_normal_cases():
    """Test normal Fibonacci number generation"""
    assert fibonacci_generator(0) == []
    assert fibonacci_generator(1) == [0]
    assert fibonacci_generator(2) == [0, 1]
    assert fibonacci_generator(5) == [0, 1, 1, 2, 3]
    assert fibonacci_generator(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_generator_larger_sequence():
    """Test a larger Fibonacci sequence"""
    result = fibonacci_generator(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_generator_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(5.5)
    
    with pytest.raises(ValueError, match="Number of Fibonacci numbers must be non-negative"):
        fibonacci_generator(-1)