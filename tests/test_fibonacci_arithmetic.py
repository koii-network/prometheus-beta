import pytest
from src.fibonacci_arithmetic import fibonacci_arithmetic_progression

def test_basic_fibonacci_arithmetic_progression():
    # First three Fibonacci numbers (1, 1, 2) form an arithmetic progression
    assert fibonacci_arithmetic_progression(3) == [1, 1, 2]

def test_invalid_input():
    # Test that invalid input raises ValueError
    with pytest.raises(ValueError):
        fibonacci_arithmetic_progression(0)
    with pytest.raises(ValueError):
        fibonacci_arithmetic_progression(-1)

def test_no_arithmetic_progression():
    # Subsequent Fibonacci numbers do not form an arithmetic progression
    assert fibonacci_arithmetic_progression(4) == []

def test_single_number():
    # Test single number case
    assert fibonacci_arithmetic_progression(1) == [1]

def test_two_numbers():
    # First two Fibonacci numbers always form an arithmetic progression
    assert fibonacci_arithmetic_progression(2) == [1, 1]