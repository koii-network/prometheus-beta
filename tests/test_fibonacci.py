import pytest
from src.fibonacci import generate_fibonacci_sequence

def test_fibonacci_sequence_valid_inputs():
    # Test different valid inputs
    assert generate_fibonacci_sequence(1) == [0]
    assert generate_fibonacci_sequence(2) == [0, 1]
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_sequence_large_input():
    # Test a larger input
    sequence = generate_fibonacci_sequence(10)
    assert len(sequence) == 10
    assert sequence == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_sequence_invalid_inputs():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Number of terms must be a positive integer"):
        generate_fibonacci_sequence(0)
    
    with pytest.raises(ValueError, match="Number of terms must be a positive integer"):
        generate_fibonacci_sequence(-1)
    
    with pytest.raises(ValueError, match="Number of terms must be a positive integer"):
        generate_fibonacci_sequence(1.5)
    
    with pytest.raises(ValueError, match="Number of terms must be a positive integer"):
        generate_fibonacci_sequence("3")
    
    with pytest.raises(ValueError, match="Number of terms must be a positive integer"):
        generate_fibonacci_sequence(None)