import pytest
from src.prime_generator import find_primes_below_n

def test_find_primes_below_n_basic():
    assert find_primes_below_n(10) == [2, 3, 5, 7]
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_find_primes_below_n_edge_cases():
    # Test lower bound cases
    assert find_primes_below_n(2) == []
    assert find_primes_below_n(1) == []
    
    # Test small prime lists
    assert find_primes_below_n(3) == [2]

def test_find_primes_below_n_large_number():
    primes_100 = find_primes_below_n(100)
    assert len(primes_100) == 25  # There are 25 primes below 100
    assert primes_100[-1] == 97  # Largest prime below 100

def test_find_primes_below_n_error_handling():
    # Test invalid input types
    with pytest.raises(TypeError):
        find_primes_below_n("not a number")
    
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)

def test_find_primes_below_n_negative():
    # Test negative numbers
    assert find_primes_below_n(-5) == []