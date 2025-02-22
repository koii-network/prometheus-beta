import pytest
from src.find_primes import find_primes_below_n

def test_find_primes_below_n_basic():
    assert find_primes_below_n(10) == [2, 3, 5, 7]
    assert find_primes_below_n(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_find_primes_edge_cases():
    assert find_primes_below_n(2) == []
    assert find_primes_below_n(1) == []
    
def test_find_primes_large_n():
    primes_below_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert find_primes_below_n(100) == primes_below_100

def test_find_primes_invalid_input():
    with pytest.raises(TypeError):
        find_primes_below_n(3.14)
    with pytest.raises(TypeError):
        find_primes_below_n("10")
    with pytest.raises(TypeError):
        find_primes_below_n(None)