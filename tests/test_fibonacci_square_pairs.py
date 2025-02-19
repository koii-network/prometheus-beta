import pytest
import math
from src.fibonacci_square_pairs import generate_fibonacci_square_pairs

def is_perfect_square(num):
    """Check if a number is a perfect square."""
    return int(math.sqrt(num))**2 == num

def test_generate_fibonacci_square_pairs_basic():
    """Test basic functionality of the sequence generator."""
    sequence = generate_fibonacci_square_pairs(5)
    
    # Check sequence length
    assert len(sequence) == 5
    
    # Check that the sum of consecutive pairs is a perfect square
    for i in range(1, len(sequence)):
        pair_sum = sequence[i-1] + sequence[i]
        assert is_perfect_square(pair_sum), f"Sum of {sequence[i-1]} and {sequence[i]} is {pair_sum}, which is not a perfect square"

def test_generate_fibonacci_square_pairs_single_element():
    """Test generating a sequence with just one element."""
    sequence = generate_fibonacci_square_pairs(1)
    assert len(sequence) == 1
    assert sequence[0] == 1

def test_generate_fibonacci_square_pairs_invalid_input():
    """Test error handling for invalid input."""
    with pytest.raises(ValueError, match="Number of elements must be at least 1"):
        generate_fibonacci_square_pairs(0)
    
    with pytest.raises(ValueError, match="Number of elements must be at least 1"):
        generate_fibonacci_square_pairs(-1)

def test_generate_fibonacci_square_pairs_larger_sequence():
    """Test generating a larger sequence."""
    sequence = generate_fibonacci_square_pairs(10)
    
    # Check sequence length
    assert len(sequence) == 10
    
    # Check that the sum of consecutive pairs is a perfect square
    for i in range(1, len(sequence)):
        pair_sum = sequence[i-1] + sequence[i]
        assert is_perfect_square(pair_sum), f"Failed at index {i}: {sequence[i-1]} + {sequence[i]} = {pair_sum}"