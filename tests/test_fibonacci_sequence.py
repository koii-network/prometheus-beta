import pytest
from src.fibonacci_sequence import generate_fibonacci_like_sequence

def test_basic_sequence():
    # Basic scenario
    result = generate_fibonacci_like_sequence(5, 2)
    assert result == [1, 1, 2, 3, 5]

def test_small_k():
    # When k is small, it should generate standard Fibonacci sequence
    result = generate_fibonacci_like_sequence(6, 1)
    assert result == [1, 1, 2, 3, 5, 8]

def test_large_k():
    # When k is large, it might limit the sequence
    result = generate_fibonacci_like_sequence(10, 10)
    assert result == [1, 1, 2, 3, 5, 8, 13, 21]

def test_minimal_n():
    # Test with smallest possible n
    result = generate_fibonacci_like_sequence(1, 1)
    assert result == [1]

def test_invalid_inputs():
    # Test invalid inputs
    with pytest.raises(ValueError):
        generate_fibonacci_like_sequence(0, 1)
    
    with pytest.raises(ValueError):
        generate_fibonacci_like_sequence(1, 0)

def test_large_n_constraint():
    # Test that sequence respects max length even if condition is met
    result = generate_fibonacci_like_sequence(3, 1)
    assert result == [1, 1, 2]