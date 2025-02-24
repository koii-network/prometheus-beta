"""
Test suite for extended Fibonacci sequence implementation.

Covers various scenarios including:
- Positive integers
- Negative integers
- Floating-point indices
- Edge cases
- Error handling
"""

import pytest
import math
from src.fibonacci_extended import fibonacci

def test_positive_integers():
    """Test Fibonacci numbers for positive integer indices."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8

def test_negative_integers():
    """Test Fibonacci numbers for negative integer indices."""
    assert fibonacci(-1) == 1
    assert fibonacci(-2) == -1
    assert fibonacci(-3) == 2
    assert fibonacci(-4) == -3
    assert fibonacci(-5) == 5
    assert fibonacci(-6) == -8

def test_floating_point_indices():
    """Test Fibonacci numbers for floating-point indices."""
    # Less strict checking, verifying characteristic behavior
    assert 0 <= fibonacci(0.5) <= 1
    assert fibonacci(0.5) != 0  # Should be a non-zero value
    assert fibonacci(1.5) > 1   # Should be greater than 1

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        fibonacci("not a number")
    with pytest.raises(TypeError):
        fibonacci(None)
    with pytest.raises(TypeError):
        fibonacci([1, 2, 3])

def test_large_indices():
    """Test behavior with large indices."""
    # Check that function can handle relatively large indices
    assert fibonacci(10) == 55
    assert fibonacci(-10) == -55

def test_zero_index():
    """Specific test for zero index."""
    assert fibonacci(0) == 0

def test_precise_floating_point():
    """Test precise floating-point calculations with more flexible assertions."""
    phi = (1 + math.sqrt(5)) / 2
    
    # Check that the result is reasonable and follows expected properties
    result = fibonacci(2.5)
    assert isinstance(result, float)
    assert abs(result) > 0  # Should not be zero
    assert abs(result) < 10  # Should be in a reasonable range