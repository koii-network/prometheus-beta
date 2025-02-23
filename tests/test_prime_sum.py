import pytest
from src.prime_sum import sum_of_primes

def test_small_valid_input():
    """Test sum of primes for a small valid input."""
    assert sum_of_primes(10) == 17  # 2 + 3 + 5 + 7 = 17

def test_edge_case_two():
    """Test the smallest valid input."""
    assert sum_of_primes(2) == 2

def test_larger_input():
    """Test sum of primes for a larger input."""
    assert sum_of_primes(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77

def test_invalid_input_less_than_two():
    """Test that ValueError is raised for input less than 2."""
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sum_of_primes(1)

def test_invalid_input_negative():
    """Test that ValueError is raised for negative input."""
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        sum_of_primes(-5)

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer input."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes("10")