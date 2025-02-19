import pytest
from src.prime_finder import find_primes_below_n

def test_find_primes_below_n_basic():
    """Test basic prime number generation"""
    assert find_primes_below_n(10) == [2, 3, 5, 7]
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_find_primes_below_n_edge_cases():
    """Test edge cases"""
    assert find_primes_below_n(2) == []
    assert find_primes_below_n(3) == [2]

def test_find_primes_below_n_invalid_inputs():
    """Test invalid input handling"""
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        find_primes_below_n(1)
    
    with pytest.raises(ValueError, match="Input must be 2 or greater"):
        find_primes_below_n(0)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_primes_below_n(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        find_primes_below_n("not a number")