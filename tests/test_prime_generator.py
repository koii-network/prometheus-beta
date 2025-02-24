import pytest
from src.prime_generator import generate_primes

def test_generate_primes_default():
    """Test default prime generation up to 100"""
    primes = generate_primes()
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    assert primes == expected_primes, "Default prime generation incorrect"

def test_generate_primes_small_numbers():
    """Test prime generation for small numbers"""
    assert generate_primes(10) == [2, 3, 5, 7], "Prime generation for small numbers incorrect"

def test_generate_primes_large_numbers():
    """Test prime generation for larger numbers"""
    large_primes = generate_primes(200)
    assert 193 in large_primes, "Large prime number missing"
    assert 199 in large_primes, "Large prime number missing"

def test_generate_primes_invalid_input():
    """Test error handling for invalid inputs"""
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_primes("100")
    
    # Test input less than 2
    with pytest.raises(ValueError, match="Maximum number must be at least 2"):
        generate_primes(1)
    
    # Test negative input
    with pytest.raises(ValueError, match="Maximum number must be at least 2"):
        generate_primes(-10)

def test_generate_primes_boundary_cases():
    """Test boundary cases"""
    # Test lower boundary
    assert generate_primes(2) == [2], "Lower boundary prime generation incorrect"
    
    # Test mid-range
    mid_primes = generate_primes(50)
    assert 47 in mid_primes, "Mid-range prime number missing"
    assert len(mid_primes) > 10, "Not enough primes generated for mid-range"