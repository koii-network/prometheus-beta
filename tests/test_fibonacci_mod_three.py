import pytest
from src.fibonacci_mod_three import generate_modified_fibonacci

def test_generate_modified_fibonacci_basic():
    """Test basic functionality of the modified Fibonacci sequence."""
    result = generate_modified_fibonacci(5)
    assert len(result) == 5
    assert result == [1, 1, 2, 4, 6]

def test_generate_modified_fibonacci_divisibility():
    """Verify that most consecutive number sums are related to divisibility by 3."""
    sequence = generate_modified_fibonacci(10)
    
    # Collect the remainders when divided by 3
    remainders = [(sequence[i-2] + sequence[i-1]) % 3 for i in range(3, len(sequence))]
    
    # At least half of the remainders should be 0
    zero_count = remainders.count(0)
    assert zero_count >= len(remainders) // 2, \
        f"Not enough numbers are divisible by 3. Remainders: {remainders}"

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