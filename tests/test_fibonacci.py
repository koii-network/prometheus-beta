import pytest
from src.fibonacci import generate_fibonacci_sequence

def test_generate_fibonacci_sequence():
    # Test standard cases
    assert generate_fibonacci_sequence(0) == []
    assert generate_fibonacci_sequence(1) == [0]
    assert generate_fibonacci_sequence(2) == [0, 1]
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_sequence_negative_input():
    # Test negative input raises ValueError
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_generate_fibonacci_sequence_large_input():
    # Test a larger sequence to ensure correct generation
    fib_10 = generate_fibonacci_sequence(10)
    assert len(fib_10) == 10
    assert fib_10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]