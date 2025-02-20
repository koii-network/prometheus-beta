import pytest
from src.count_factors import count_factors

def test_count_factors_prime_number():
    """Test a prime number, which should have 2 factors."""
    assert count_factors(7) == 2

def test_count_factors_perfect_square():
    """Test a perfect square, which has an odd number of factors."""
    assert count_factors(9) == 3

def test_count_factors_composite_number():
    """Test a composite number with multiple factors."""
    assert count_factors(12) == 6

def test_count_factors_one():
    """Test the edge case of 1, which has only 1 factor."""
    assert count_factors(1) == 1

def test_count_factors_invalid_input():
    """Test that invalid inputs raise a ValueError."""
    with pytest.raises(ValueError):
        count_factors(0)
    
    with pytest.raises(ValueError):
        count_factors(-5)
    
    with pytest.raises(ValueError):
        count_factors(3.14)
    
    with pytest.raises(ValueError):
        count_factors("not a number")