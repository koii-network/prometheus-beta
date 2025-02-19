import pytest
from src.sum_primes import sum_of_primes

def test_sum_of_primes_basic():
    """Test basic scenarios of prime number summation."""
    assert sum_of_primes(10) == 17  # 2 + 3 + 5 + 7
    assert sum_of_primes(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_sum_of_primes_edge_cases():
    """Test edge case scenarios."""
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sum_of_primes(1)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sum_of_primes(0)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        sum_of_primes(-5)

def test_sum_of_primes_type_checking():
    """Test type checking for input."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes("10")

def test_sum_of_primes_larger_number():
    """Test summation for a larger number."""
    assert sum_of_primes(100) == 1060