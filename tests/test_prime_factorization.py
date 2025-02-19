import pytest
from src.prime_factorization import prime_factorize

def test_prime_factorize_basic_cases():
    assert prime_factorize(2) == (2,)
    assert prime_factorize(4) == (2, 2)
    assert prime_factorize(12) == (2, 2, 3)
    assert prime_factorize(15) == (3, 5)
    assert prime_factorize(100) == (2, 2, 5, 5)

def test_prime_factorize_prime_numbers():
    assert prime_factorize(17) == (17,)
    assert prime_factorize(29) == (29,)
    assert prime_factorize(97) == (97,)

def test_prime_factorize_large_number():
    assert prime_factorize(84) == (2, 2, 3, 7)
    assert prime_factorize(360) == (2, 2, 2, 3, 3, 5)

def test_prime_factorize_error_cases():
    with pytest.raises(ValueError, match="Input must be a positive integer greater than or equal to 2"):
        prime_factorize(1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than or equal to 2"):
        prime_factorize(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer greater than or equal to 2"):
        prime_factorize(-5)

def test_prime_factorize_type_error():
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorize(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorize("not a number")