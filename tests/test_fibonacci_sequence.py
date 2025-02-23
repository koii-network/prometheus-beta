import pytest
from src.fibonacci_sequence import generate_modified_fibonacci

def test_basic_sequence():
    assert generate_modified_fibonacci(5, 2) == [1, 1, 2, 3, 5]

def test_small_k():
    assert generate_modified_fibonacci(4, 1) == [1, 1, 2, 3]

def test_large_k():
    assert generate_modified_fibonacci(3, 10) == [1, 1]

def test_max_length():
    sequence = generate_modified_fibonacci(10, 2)
    assert len(sequence) <= 10

def test_consecutive_sum():
    sequence = generate_modified_fibonacci(6, 5)
    for i in range(1, len(sequence)):
        assert sequence[i-1] + sequence[i] >= 5

def test_invalid_n_negative():
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1, 2)

def test_invalid_n_zero():
    with pytest.raises(ValueError):
        generate_modified_fibonacci(0, 2)

def test_invalid_k_negative():
    with pytest.raises(ValueError):
        generate_modified_fibonacci(5, -1)

def test_invalid_k_zero():
    with pytest.raises(ValueError):
        generate_modified_fibonacci(5, 0)

def test_invalid_types():
    with pytest.raises(ValueError):
        generate_modified_fibonacci("5", 2)
    with pytest.raises(ValueError):
        generate_modified_fibonacci(5, "2")