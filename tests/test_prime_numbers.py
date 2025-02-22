import pytest
from src.prime_numbers import generate_primes

def test_generate_primes_default():
    """Test prime number generation with default limit of 100"""
    primes = generate_primes()
    
    # Known primes in the first 100 numbers
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97
    ]
    
    assert primes == expected_primes, "Default prime generation failed"
    assert len(primes) == 25, "Incorrect number of primes generated"

def test_generate_primes_small_limit():
    """Test prime generation with small limits"""
    assert generate_primes(1) == [], "Primes below 2 should return empty list"
    assert generate_primes(2) == [2], "Failed to handle limit of 2"

def test_generate_primes_larger_limit():
    """Test prime generation with a larger limit"""
    primes_150 = generate_primes(150)
    
    # Verify some known primes above 100
    additional_primes = [101, 103, 107, 109, 113]
    for prime in additional_primes:
        assert prime in primes_150, f"{prime} should be in primes up to 150"

def test_generate_primes_type_handling():
    """Test type handling and edge cases"""
    with pytest.raises(TypeError):
        generate_primes("100")  # Should not accept string input
    
    with pytest.raises(TypeError):
        generate_primes(None)  # Should not accept None

def test_generate_primes_negative_limit():
    """Test handling of negative limits"""
    assert generate_primes(-10) == [], "Negative limits should return empty list"