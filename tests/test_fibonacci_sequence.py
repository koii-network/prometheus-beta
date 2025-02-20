import pytest
from src.fibonacci_sequence import generate_fibonacci_sequence

def test_basic_sequence():
    # Basic test with small values
    result = generate_fibonacci_sequence(5, 3)
    assert result == [1, 1, 2, 3, 5]

def test_sequence_with_small_k():
    # Test with a small k value
    result = generate_fibonacci_sequence(6, 2)
    assert result == [1, 1, 2, 3, 5, 8]

def test_sequence_length_constraint():
    # Test that sequence respects max length n
    result = generate_fibonacci_sequence(3, 10)
    assert result == [1, 1, 2]

def test_sequence_sum_constraint():
    # Test that sequence stops when consecutive sum is less than k
    result = generate_fibonacci_sequence(10, 100)
    assert result == [1, 1]

def test_single_element_sequence():
    # Test with n=1
    result = generate_fibonacci_sequence(1, 1)
    assert result == [1]

def test_invalid_n_parameter():
    # Test invalid n parameter
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_sequence(0, 5)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_sequence(-1, 5)
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_sequence("not a number", 5)

def test_invalid_k_parameter():
    # Test invalid k parameter
    with pytest.raises(ValueError, match="k must be a positive integer"):
        generate_fibonacci_sequence(5, 0)
    with pytest.raises(ValueError, match="k must be a positive integer"):
        generate_fibonacci_sequence(5, -1)
    with pytest.raises(ValueError, match="k must be a positive integer"):
        generate_fibonacci_sequence(5, "not a number")