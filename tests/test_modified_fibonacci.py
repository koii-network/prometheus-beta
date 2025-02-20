import pytest
from src.modified_fibonacci import modified_fibonacci

def test_modified_fibonacci_basic():
    """Test basic functionality of the modified Fibonacci sequence"""
    result = modified_fibonacci(5)
    assert result == [0, 1, 1, 2, 3], f"Expected [0, 1, 1, 2, 3], but got {result}"

def test_modified_fibonacci_sequence_property():
    """Verify that each term is the sum of the two preceding terms"""
    for n in range(3, 10):
        sequence = modified_fibonacci(n)
        for i in range(2, len(sequence)):
            assert sequence[i] == sequence[i-1] + sequence[i-2], \
                f"Term {sequence[i]} is not the sum of {sequence[i-1]} and {sequence[i-2]}"

def test_modified_fibonacci_single_term():
    """Test generating a single term"""
    result = modified_fibonacci(1)
    assert result == [0], f"Expected [0], but got {result}"

def test_modified_fibonacci_two_terms():
    """Test generating two terms"""
    result = modified_fibonacci(2)
    assert result == [0, 1], f"Expected [0, 1], but got {result}"

def test_modified_fibonacci_invalid_input():
    """Test invalid input raises ValueError"""
    with pytest.raises(ValueError, match="Number of terms must be at least 1"):
        modified_fibonacci(0)
    
    with pytest.raises(ValueError, match="Number of terms must be at least 1"):
        modified_fibonacci(-1)

def test_modified_fibonacci_longer_sequence():
    """Test a longer sequence to ensure consistency"""
    sequence = modified_fibonacci(10)
    assert len(sequence) == 10, f"Expected 10 terms, but got {len(sequence)}"
    
    # Verify Fibonacci property
    for i in range(2, len(sequence)):
        assert sequence[i] == sequence[i-1] + sequence[i-2], \
            f"Term {sequence[i]} is not the sum of {sequence[i-1]} and {sequence[i-2]}"