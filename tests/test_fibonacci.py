import pytest
from src.fibonacci import generate_fibonacci_sequence

def test_fibonacci_sequence_basic():
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]

def test_fibonacci_sequence_zero_terms():
    assert generate_fibonacci_sequence(0) == []

def test_fibonacci_sequence_one_term():
    assert generate_fibonacci_sequence(1) == [0]

def test_fibonacci_sequence_two_terms():
    assert generate_fibonacci_sequence(2) == [0, 1]

def test_fibonacci_sequence_ten_terms():
    assert generate_fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_negative_input():
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_fibonacci_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        generate_fibonacci_sequence("3")
    with pytest.raises(TypeError, match="Input must be a non-negative integer"):
        generate_fibonacci_sequence(3.14)