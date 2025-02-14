import pytest
from src.fibonacci import generate_fibonacci

def test_fibonacci_zero_terms():
    """Test generating 0 Fibonacci terms"""
    assert generate_fibonacci(0) == []

def test_fibonacci_one_term():
    """Test generating 1 Fibonacci term"""
    assert generate_fibonacci(1) == [0]

def test_fibonacci_two_terms():
    """Test generating 2 Fibonacci terms"""
    assert generate_fibonacci(2) == [0, 1]

def test_fibonacci_multiple_terms():
    """Test generating multiple Fibonacci terms"""
    assert generate_fibonacci(6) == [0, 1, 1, 2, 3, 5]

def test_fibonacci_negative_terms():
    """Test that generating negative terms raises a ValueError"""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci(-1)

def test_fibonacci_length():
    """Test that the generated sequence has the correct length"""
    for n in range(10):
        assert len(generate_fibonacci(n)) == n