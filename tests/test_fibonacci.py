import pytest
from src.fibonacci import generate_fibonacci

def test_generate_fibonacci_zero_terms():
    """Test generating Fibonacci sequence with 0 terms"""
    assert generate_fibonacci(0) == []

def test_generate_fibonacci_one_term():
    """Test generating Fibonacci sequence with 1 term"""
    assert generate_fibonacci(1) == [0]

def test_generate_fibonacci_two_terms():
    """Test generating Fibonacci sequence with 2 terms"""
    assert generate_fibonacci(2) == [0, 1]

def test_generate_fibonacci_multiple_terms():
    """Test generating Fibonacci sequence with multiple terms"""
    assert generate_fibonacci(6) == [0, 1, 1, 2, 3, 5]

def test_generate_fibonacci_larger_sequence():
    """Test generating a larger Fibonacci sequence"""
    result = generate_fibonacci(10)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert result == expected

def test_generate_fibonacci_negative_input():
    """Test that negative input raises a ValueError"""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci(-1)

def test_generate_fibonacci_invalid_type():
    """Test that non-integer input raises a TypeError"""
    with pytest.raises(TypeError, match="Number of terms must be an integer"):
        generate_fibonacci("5")
    with pytest.raises(TypeError, match="Number of terms must be an integer"):
        generate_fibonacci(5.5)
    with pytest.raises(TypeError, match="Number of terms must be an integer"):
        generate_fibonacci(None)