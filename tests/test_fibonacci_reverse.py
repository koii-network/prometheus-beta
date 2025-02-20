import pytest
from src.fibonacci_reverse import fibonacci_reverse

def test_fibonacci_reverse_basic():
    assert fibonacci_reverse(5) == [5, 3, 2, 1, 0]

def test_fibonacci_reverse_zero():
    assert fibonacci_reverse(0) == []

def test_fibonacci_reverse_one():
    assert fibonacci_reverse(1) == [0]

def test_fibonacci_reverse_two():
    assert fibonacci_reverse(2) == [1, 0]

def test_fibonacci_reverse_negative_input():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_reverse(-1)

def test_fibonacci_reverse_non_integer_input():
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_reverse(5.5)

def test_fibonacci_reverse_sequence_length():
    # Test a few different sequence lengths
    assert len(fibonacci_reverse(7)) == 7
    assert len(fibonacci_reverse(10)) == 10

def test_fibonacci_reverse_large_input():
    # Test a larger input to ensure calculation works correctly
    sequence = fibonacci_reverse(10)
    assert sequence[0] == 55  # 10th Fibonacci number
    assert sequence[-1] == 0  # Sequence ends with 0