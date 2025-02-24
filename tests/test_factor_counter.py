import pytest
from src.factor_counter import count_factors

def test_count_factors_prime_number():
    """Test a prime number which should have exactly 2 factors."""
    assert count_factors(7) == 2

def test_count_factors_perfect_square():
    """Test a perfect square number."""
    assert count_factors(9) == 3

def test_count_factors_composite_number():
    """Test a composite number with multiple factors."""
    assert count_factors(12) == 6

def test_count_factors_one():
    """Test edge case for number 1."""
    assert count_factors(1) == 1

def test_count_factors_large_number():
    """Test a larger number to ensure efficiency."""
    assert count_factors(100) == 9

def test_invalid_input_zero():
    """Test that zero raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(0)

def test_invalid_input_negative():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(-5)

def test_invalid_input_non_integer():
    """Test that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_factors(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        count_factors("12")