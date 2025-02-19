import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    # Test first two Fibonacci numbers
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    # Test some known Fibonacci numbers
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

def test_fibonacci_negative_input():
    # Test that negative inputs raise a ValueError
    with pytest.raises(ValueError, match="Fibonacci is not defined for negative indices"):
        fibonacci(-1)

def test_fibonacci_non_integer_input():
    # Test that non-integer inputs raise a TypeError
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci([5])