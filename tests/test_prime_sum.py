import pytest
from src.prime_sum import sum_primes_up_to

def test_sum_primes_up_to_basic():
    """Test basic functionality with small numbers."""
    assert sum_primes_up_to(10) == 17  # 2 + 3 + 5 + 7 = 17
    assert sum_primes_up_to(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77

def test_sum_primes_up_to_edge_cases():
    """Test edge cases."""
    assert sum_primes_up_to(1) == 0  # No primes less than or equal to 1
    assert sum_primes_up_to(2) == 2  # First prime number
    assert sum_primes_up_to(0) == 0
    assert sum_primes_up_to(-5) == 0

def test_sum_primes_up_to_larger_number():
    """Test with a larger number to ensure performance."""
    assert sum_primes_up_to(100) == 1060  # Sum of primes up to 100

def test_sum_primes_up_to_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        sum_primes_up_to(3.14)
    
    with pytest.raises(ValueError):
        sum_primes_up_to("not a number")
    
    with pytest.raises(ValueError):
        sum_primes_up_to(None)