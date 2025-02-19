import pytest
import math
from src.fibonacci_square_pairs import generate_fibonacci_square_pairs

def is_perfect_square(num):
    """Helper function to check if a number is a perfect square"""
    return int(math.sqrt(num)) ** 2 == num

def test_generate_fibonacci_square_pairs_basic():
    """Test basic sequence generation"""
    sequence = generate_fibonacci_square_pairs(5)
    assert len(sequence) == 5
    
    # Check that consecutive pair sums are perfect squares
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"

def test_generate_fibonacci_square_pairs_minimal():
    """Test minimal sequence generation"""
    sequence = generate_fibonacci_square_pairs(1)
    assert len(sequence) == 1
    assert sequence == [1]

def test_generate_fibonacci_square_pairs_error():
    """Test error handling for invalid input"""
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_square_pairs(0)
    
    with pytest.raises(ValueError, match="n must be a positive integer"):
        generate_fibonacci_square_pairs(-1)

def test_generate_fibonacci_square_pairs_longer_sequence():
    """Test a longer sequence to ensure square pair sum property"""
    sequence = generate_fibonacci_square_pairs(10)
    assert len(sequence) == 10
    
    # Check that every consecutive pair creates a perfect square sum
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} at index {i} is not a perfect square"