import pytest
from src.modified_fibonacci import modified_fibonacci

def test_modified_fibonacci_basic():
    # Test first few terms of the sequence
    result = modified_fibonacci(5)
    assert result == [0, 1, 1, 2, 3], f"Expected [0, 1, 1, 2, 3], but got {result}"

def test_modified_fibonacci_odd_sum():
    # Verify that the sum of any two consecutive terms is always odd
    for n in range(2, 10):
        seq = modified_fibonacci(n)
        for i in range(1, len(seq)):
            assert (seq[i-1] + seq[i]) % 2 == 1, \
                f"Sum of {seq[i-1]} and {seq[i]} is not odd at index {i}"

def test_modified_fibonacci_single_term():
    # Test with single term
    result = modified_fibonacci(1)
    assert result == [0], f"Expected [0], but got {result}"

def test_modified_fibonacci_multiple_terms():
    # Test with multiple terms
    result = modified_fibonacci(7)
    expected = [0, 1, 1, 2, 3, 5, 8]
    assert result == expected, f"Expected {expected}, but got {result}"

def test_modified_fibonacci_invalid_input():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        modified_fibonacci(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        modified_fibonacci(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        modified_fibonacci(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        modified_fibonacci("not a number")