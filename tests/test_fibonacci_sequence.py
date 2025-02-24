import pytest
from src.fibonacci_sequence import generate_fibonacci_sequence

def test_basic_sequence():
    """Test a basic sequence generation"""
    assert generate_fibonacci_sequence(5, 2) == [1, 1, 2, 3, 5]

def test_sum_constraint():
    """Test that consecutive numbers sum is >= k"""
    result = generate_fibonacci_sequence(10, 5)
    for i in range(1, len(result)):
        if len(result) > 1:
            assert result[i] + result[i-1] >= 5, f"Failed at index {i}"

def test_max_length_constraint():
    """Test that sequence length does not exceed n"""
    result = generate_fibonacci_sequence(3, 1)
    assert len(result) == 3

def test_small_k():
    """Test sequence with small k"""
    result = generate_fibonacci_sequence(6, 1)
    assert result == [1, 1, 2, 3, 5, 8]

def test_large_k():
    """Test sequence with large k that limits growth"""
    result = generate_fibonacci_sequence(5, 100)
    assert len(result) == 1 and result[0] == 1

def test_zero_length():
    """Test zero-length sequence"""
    assert generate_fibonacci_sequence(0, 5) == []

def test_invalid_n():
    """Test invalid n parameter"""
    with pytest.raises(ValueError):
        generate_fibonacci_sequence(-1, 5)
    with pytest.raises(ValueError):
        generate_fibonacci_sequence(0.5, 5)
    with pytest.raises(ValueError):
        generate_fibonacci_sequence('invalid', 5)

def test_invalid_k():
    """Test invalid k parameter"""
    with pytest.raises(ValueError):
        generate_fibonacci_sequence(5, -1)
    with pytest.raises(ValueError):
        generate_fibonacci_sequence(5, 0)
    with pytest.raises(ValueError):
        generate_fibonacci_sequence(5, 0.5)
    with pytest.raises(ValueError):
        generate_fibonacci_sequence(5, 'invalid')