import pytest
from src.fibonacci import generate_fibonacci_sequence

def test_generate_fibonacci_sequence_zero_terms():
    assert generate_fibonacci_sequence(0) == []

def test_generate_fibonacci_sequence_one_term():
    assert generate_fibonacci_sequence(1) == [0]

def test_generate_fibonacci_sequence_two_terms():
    assert generate_fibonacci_sequence(2) == [0, 1]

def test_generate_fibonacci_sequence_multiple_terms():
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_generate_fibonacci_sequence_negative_input():
    with pytest.raises(ValueError, match="Number of terms must be a non-negative integer"):
        generate_fibonacci_sequence(-1)