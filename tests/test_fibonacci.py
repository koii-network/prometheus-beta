import pytest
from src.fibonacci import fibonacci_dp

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence."""
    assert fibonacci_dp(0) == 0
    assert fibonacci_dp(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values."""
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (10, 55)
    ]
    
    for n, expected in test_cases:
        assert fibonacci_dp(n) == expected, f"Failed for n={n}"

def test_fibonacci_input_validation():
    """Test input validation and error handling."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_dp(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_dp(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_dp("5")

def test_fibonacci_large_number():
    """Test Fibonacci calculation for a larger number."""
    # Verify a larger Fibonacci number without checking the exact value
    result = fibonacci_dp(20)
    assert isinstance(result, int)
    assert result > 0