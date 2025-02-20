import pytest
from src.fibonacci_odd_sequence import generate_odd_fibonacci_sequence

def test_generate_odd_fibonacci_sequence_basic():
    """Test basic functionality of generating odd Fibonacci sequence."""
    result = generate_odd_fibonacci_sequence(5)
    assert result == [1, 1, 3, 5, 13]
    
    # Verify all numbers are odd
    assert all(num % 2 != 0 for num in result)

def test_generate_odd_fibonacci_sequence_zero():
    """Test generating sequence of length 0."""
    assert generate_odd_fibonacci_sequence(0) == []

def test_generate_odd_fibonacci_sequence_one():
    """Test generating sequence of length 1."""
    assert generate_odd_fibonacci_sequence(1) == [1]

def test_generate_odd_fibonacci_sequence_negative():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_odd_fibonacci_sequence(-1)

def test_generate_odd_fibonacci_sequence_larger():
    """Test generating a larger sequence of odd Fibonacci numbers."""
    result = generate_odd_fibonacci_sequence(10)
    assert len(result) == 10
    assert all(num % 2 != 0 for num in result)
    
    # Verify the Fibonacci property
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2]