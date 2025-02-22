import pytest
import math
from src.fibonacci_square_pairs import generate_fibonacci_square_pairs, is_perfect_square

def test_is_perfect_square():
    """Test the is_perfect_square helper function."""
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    assert is_perfect_square(7) == False
    assert is_perfect_square(15) == False

def test_generate_fibonacci_square_pairs_basic():
    """Test basic functionality of the sequence generator."""
    sequence = generate_fibonacci_square_pairs(5)
    assert len(sequence) == 5
    
    # Check that sums of consecutive pairs are perfect squares
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"

def test_generate_fibonacci_square_pairs_small_input():
    """Test sequence generation with small inputs."""
    # Minimum valid input
    sequence = generate_fibonacci_square_pairs(2)
    assert len(sequence) == 2
    assert sequence == [1, 1]

def test_generate_fibonacci_square_pairs_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="n must be at least 2"):
        generate_fibonacci_square_pairs(1)
    
    with pytest.raises(ValueError, match="n must be at least 2"):
        generate_fibonacci_square_pairs(0)

def test_generate_fibonacci_square_pairs_longer_sequence():
    """Test generation of a longer sequence."""
    sequence = generate_fibonacci_square_pairs(10)
    assert len(sequence) == 10
    
    # Check that sums of consecutive pairs are perfect squares
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        assert is_perfect_square(pair_sum), f"Pair sum {pair_sum} is not a perfect square"