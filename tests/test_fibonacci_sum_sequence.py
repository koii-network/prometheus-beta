import pytest
from src.fibonacci_sum_sequence import generate_fibonacci_sum_sequence

def test_basic_sequence():
    # Test a simple case
    result = generate_fibonacci_sum_sequence(5, 3)
    assert len(result) <= 5
    assert all(result[i] + result[i+1] >= 3 for i in range(len(result)-1))

def test_zero_length():
    # Test zero length sequence
    assert generate_fibonacci_sum_sequence(0, 5) == []

def test_zero_k():
    # Test when k is zero
    result = generate_fibonacci_sum_sequence(5, 0)
    assert len(result) > 0
    assert result[0] == 0

def test_high_k():
    # Test with a high k value
    result = generate_fibonacci_sum_sequence(10, 100)
    assert len(result) > 0
    assert all(result[i] + result[i+1] >= 100 for i in range(len(result)-1))

def test_negative_input():
    # Test negative inputs
    with pytest.raises(ValueError):
        generate_fibonacci_sum_sequence(-1, 5)
    
    with pytest.raises(ValueError):
        generate_fibonacci_sum_sequence(5, -1)

def test_sequence_constraints():
    # Detailed test of sequence constraints
    n, k = 6, 5
    result = generate_fibonacci_sum_sequence(n, k)
    
    assert len(result) <= n
    for i in range(1, len(result)):
        assert result[i-1] + result[i] >= k, f"Failed at index {i}"

def test_minimum_sequence_length():
    # Ensure meaningful sequence is generated
    result = generate_fibonacci_sum_sequence(5, 10)
    assert len(result) > 0
    assert all(result[i] + result[i+1] >= 10 for i in range(len(result)-1))