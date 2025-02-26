import pytest
from src.odd_sum_fibonacci import generate_odd_sum_fibonacci

def test_generate_odd_sum_fibonacci_basic():
    """Test basic sequence generation"""
    result = generate_odd_sum_fibonacci(5)
    # The exact sequence might vary based on the specific implementation
    assert len(result) == 5
    assert result[0] == 0
    assert result[1] == 1

def test_generate_odd_sum_fibonacci_odd_sum_rule():
    """Verify that sum of consecutive elements is always different from the sum adjacent to it"""
    result = generate_odd_sum_fibonacci(10)
    for i in range(len(result) - 2):
        # Ensure the sum of pairs change their parity
        assert (result[i] + result[i+1]) % 2 != (result[i+1] + result[i+2]) % 2, \
            f"Consecutive sum parity should alternate"

def test_generate_odd_sum_fibonacci_edge_cases():
    """Test edge cases"""
    # Empty sequence
    assert generate_odd_sum_fibonacci(0) == [], "Empty sequence should return empty list"
    
    # Single element
    assert generate_odd_sum_fibonacci(1) == [0], "Single element sequence should be [0]"
    
    # Two elements
    assert generate_odd_sum_fibonacci(2) == [0, 1], "Two-element sequence should be [0, 1]"

def test_generate_odd_sum_fibonacci_invalid_input():
    """Test error handling for invalid inputs"""
    # Negative input
    with pytest.raises(ValueError, match="Number of elements must be non-negative"):
        generate_odd_sum_fibonacci(-1)
    
    # Non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci(3.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_odd_sum_fibonacci("5")

def test_generate_odd_sum_fibonacci_length():
    """Verify correct sequence length"""
    for n in range(1, 10):
        result = generate_odd_sum_fibonacci(n)
        assert len(result) == n, f"Sequence length should be {n}"