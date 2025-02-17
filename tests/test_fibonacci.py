import pytest
from src.fibonacci import generate_fibonacci_sequence

def test_fibonacci_zero_terms():
    assert generate_fibonacci_sequence(0) == []

def test_fibonacci_one_term():
    assert generate_fibonacci_sequence(1) == [0]

def test_fibonacci_two_terms():
    assert generate_fibonacci_sequence(2) == [0, 1]

def test_fibonacci_multiple_terms():
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_raises_error_for_negative_terms():
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_fibonacci_large_sequence():
    sequence = generate_fibonacci_sequence(10)
    assert len(sequence) == 10
    assert sequence == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]