import pytest
from src.fibonacci import recursive_fibonacci

def test_recursive_fibonacci_base_cases():
    """Test the base cases of the Fibonacci sequence."""
    assert recursive_fibonacci(0) == 0
    assert recursive_fibonacci(1) == 1

def test_recursive_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    # Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34)
    ]
    
    for n, expected in test_cases:
        assert recursive_fibonacci(n) == expected, f"Failed for n={n}"

def test_recursive_fibonacci_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        recursive_fibonacci(-1)

def test_recursive_fibonacci_invalid_input_type():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        recursive_fibonacci(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        recursive_fibonacci("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        recursive_fibonacci(None)