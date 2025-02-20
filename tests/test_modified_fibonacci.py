import pytest
from src.modified_fibonacci import generate_modified_fibonacci

def test_modified_fibonacci_sequence_length():
    """Test that the function returns the correct number of terms."""
    for n in range(1, 10):
        sequence = generate_modified_fibonacci(n)
        assert len(sequence) == n, f"Failed for n={n}"

def test_modified_fibonacci_first_two_terms():
    """Test that the first two terms are always 0 and 1."""
    sequence = generate_modified_fibonacci(5)
    assert sequence[:2] == [0, 1], "First two terms must be 0 and 1"

def test_modified_fibonacci_invalid_input():
    """Test that the function raises ValueError for invalid input."""
    with pytest.raises(ValueError):
        generate_modified_fibonacci(0)
    
    with pytest.raises(ValueError):
        generate_modified_fibonacci(-1)

def test_modified_fibonacci_generates_correct_initial_sequence():
    """Test the initial terms of the modified Fibonacci sequence."""
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    result = generate_modified_fibonacci(10)
    assert result == expected_sequence, f"Expected {expected_sequence}, got {result}"