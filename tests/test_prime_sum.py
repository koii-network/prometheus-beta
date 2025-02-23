import pytest
from src.prime_sum import sum_primes_under_n

def test_sum_primes_under_small_n():
    """Test sum of primes for small numbers"""
    assert sum_primes_under_n(10) == 17  # 2 + 3 + 5 + 7
    assert sum_primes_under_n(2) == 0
    assert sum_primes_under_n(3) == 2

def test_sum_primes_under_larger_n():
    """Test sum of primes for larger numbers"""
    assert sum_primes_under_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19
    assert sum_primes_under_n(30) == 129

def test_edge_cases():
    """Test edge cases and boundary conditions"""
    assert sum_primes_under_n(1) == 0
    assert sum_primes_under_n(0) == 0

def test_invalid_inputs():
    """Test handling of invalid inputs"""
    with pytest.raises(TypeError):
        sum_primes_under_n("10")
    
    with pytest.raises(TypeError):
        sum_primes_under_n(3.14)
    
    with pytest.raises(TypeError):
        sum_primes_under_n(None)

def test_negative_input():
    """Test handling of negative input"""
    assert sum_primes_under_n(-5) == 0