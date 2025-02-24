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
    # Check some known floating-point values
    assert math.isclose(fibonacci(0.5), 0.5688444, rel_tol=1e-6)
    assert math.isclose(fibonacci(1.5), 1.272020, rel_tol=1e-6)
    assert math.isclose(fibonacci(-0.5), -0.5688444, rel_tol=1e-6)

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
    """Test precise floating-point calculations."""
    phi = (1 + math.sqrt(5)) / 2
    # Check some specific floating-point calculations
    assert math.isclose(
        fibonacci(2.5), 
        (phi**2.5 - (1-phi)**2.5) / math.sqrt(5), 
        rel_tol=1e-6
    )