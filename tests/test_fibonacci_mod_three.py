import pytest
from src.fibonacci_mod_three import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    """Test basic functionality of the modified Fibonacci sequence."""
    result = generate_modified_fibonacci(5)
    assert len(result) == 5
    assert result == [1, 1, 2, 4, 6]

def test_generate_modified_fibonacci_divisibility():
    """Verify that the sum of consecutive numbers is divisible by 3."""
    sequence = generate_modified_fibonacci(6)
    for i in range(2, len(sequence)):
        assert (sequence[i-2] + sequence[i-1]) % 3 == 0

def test_generate_modified_fibonacci_zero():
    """Test generating sequence with zero elements."""
    assert generate_modified_fibonacci(0) == []

def test_generate_modified_fibonacci_single():
    """Test generating sequence with a single element."""
    assert generate_modified_fibonacci(1) == [1]

def test_generate_modified_fibonacci_two():
    """Test generating sequence with two elements."""
    assert generate_modified_fibonacci(2) == [1, 1]

def test_generate_modified_fibonacci_negative():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of elements must be non-negative"):
        generate_modified_fibonacci(-1)

def test_generate_modified_fibonacci_large():
    """Test generating a larger sequence."""
    sequence = generate_modified_fibonacci(10)
    assert len(sequence) == 10
    
    # Verify divisibility for each consecutive triplet
    for i in range(2, len(sequence)):
        assert (sequence[i-2] + sequence[i-1]) % 3 == 0