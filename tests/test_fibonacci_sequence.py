import pytest
from src.fibonacci_sequence import fibonacci_sequence

def test_fibonacci_sequence_basic():
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_sequence_large_n():
    result = fibonacci_sequence(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_sequence_error_handling():
    with pytest.raises(ValueError):
        fibonacci_sequence(-1)

def test_fibonacci_sequence_consistency():
    # Check that repeated calls return the same result
    result1 = fibonacci_sequence(10)
    result2 = fibonacci_sequence(10)
    assert result1 == result2