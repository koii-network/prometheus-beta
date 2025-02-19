import pytest
import math
from src.fibonacci_square_pairs import generate_fibonacci_square_pairs

def is_perfect_square(num):
    """Helper function to check if a number is a perfect square"""
    sqrt = math.isqrt(num)
    return sqrt * sqrt == num

def test_generate_fibonacci_square_pairs_basic():
    """Test basic functionality of the function"""
    sequence = generate_fibonacci_square_pairs(5)
    assert len(sequence) == 5
    
    # Check consecutive pair sums are perfect squares
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"

def test_generate_fibonacci_square_pairs_minimum_length():
    """Test the function with minimum required length"""
    sequence = generate_fibonacci_square_pairs(2)
    assert len(sequence) == 2
    assert sequence == [1, 1]

def test_generate_fibonacci_square_pairs_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(ValueError, match="Sequence length must be at least 2"):
        generate_fibonacci_square_pairs(1)

def test_generate_fibonacci_square_pairs_more_elements():
    """Test generating a longer sequence"""
    sequence = generate_fibonacci_square_pairs(10)
    assert len(sequence) == 10
    
    # Check consecutive pair sums are perfect squares
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"

def test_sequence_properties():
    """Additional checks on the sequence properties"""
    sequence = generate_fibonacci_square_pairs(7)
    
    # Check that the sequence is not just a standard Fibonacci sequence
    assert not (sequence == [1, 1, 2, 3, 5, 8, 13]), "Sequence should not be standard Fibonacci"
    
    # Verify pair sum squares
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        sqrt_sum = math.isqrt(pair_sum)
        assert sqrt_sum * sqrt_sum == pair_sum, f"Pair sum {pair_sum} is not a perfect square"