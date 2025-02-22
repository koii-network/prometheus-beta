import pytest
from src.odd_fibonacci import generate_odd_fibonacci

def test_generate_odd_fibonacci_basic():
    # Test basic sequence generation
    result = generate_odd_fibonacci(5)
    assert len(result) == 5
    assert all(num % 2 == 1 for num in result)
    assert result == [1, 1, 3, 5, 11]

def test_generate_odd_fibonacci_zero_length():
    # Test zero-length sequence
    assert generate_odd_fibonacci(0) == []

def test_generate_odd_fibonacci_single_element():
    # Test single element sequence
    assert generate_odd_fibonacci(1) == [1]

def test_generate_odd_fibonacci_negative_input():
    # Test negative input raises ValueError
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_odd_fibonacci(-1)

def test_generate_odd_fibonacci_large_sequence():
    # Test a larger sequence to ensure odd number generation
    result = generate_odd_fibonacci(10)
    assert len(result) == 10
    assert all(num % 2 == 1 for num in result)

def test_odd_fibonacci_sequence_properties():
    # Verify that each number is the sum of the previous two
    result = generate_odd_fibonacci(7)
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]
        assert result[i] % 2 == 1  # Ensure all numbers are odd