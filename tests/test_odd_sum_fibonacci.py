import pytest
from src.odd_sum_fibonacci import generate_odd_sum_fibonacci

def test_generate_odd_sum_fibonacci_basic():
    """Test basic functionality of the function."""
    result = generate_odd_sum_fibonacci(5)
    assert result == [0, 1, 1, 2, 3], f"Expected [0, 1, 1, 2, 3], but got {result}"

def test_generate_odd_sum_fibonacci_odd_sum_constraint():
    """Verify that the sum of any two consecutive numbers follows the sequence."""
    result = generate_odd_sum_fibonacci(10)
    expected_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert result == expected_sequence, f"Expected {expected_sequence}, but got {result}"

def test_generate_odd_sum_fibonacci_zero_terms():
    """Test generating zero terms."""
    assert generate_odd_sum_fibonacci(0) == [], "Should return empty list for 0 terms"

def test_generate_odd_sum_fibonacci_single_term():
    """Test generating a single term."""
    assert generate_odd_sum_fibonacci(1) == [0], "Should return [0] for 1 term"

def test_generate_odd_sum_fibonacci_two_terms():
    """Test generating two terms."""
    assert generate_odd_sum_fibonacci(2) == [0, 1], "Should return [0, 1] for 2 terms"

def test_generate_odd_sum_fibonacci_negative_input():
    """Test that negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_odd_sum_fibonacci(-1)

def test_generate_odd_sum_fibonacci_non_integer_input():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci(3.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci("5")