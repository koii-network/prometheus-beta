import pytest
from src.prime_sum_pairs import generate_prime_sum_pairs, is_prime

def test_is_prime():
    """Test primality checking function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False

def test_generate_prime_sum_pairs():
    """Test prime sum pairs generation."""
    # Basic cases
    result_2 = generate_prime_sum_pairs(2)
    assert len(result_2) > 0 and is_prime(result_2[0])
    
    result_3 = generate_prime_sum_pairs(3)
    assert set(result_3).issubset({3, 5})
    assert all(is_prime(x) for x in result_3)
    
    # Slightly larger case
    result = generate_prime_sum_pairs(5)
    assert set(result).issubset({3, 5, 7, 11})
    assert all(is_prime(x) for x in result)
    
    # Verify uniqueness and sorting
    result = generate_prime_sum_pairs(10)
    assert len(result) == len(set(result)), "Result should not contain duplicates"
    assert result == sorted(result), "Result should be sorted"

def test_prime_sum_pairs_edge_cases():
    """Test edge cases for prime sum pairs generation."""
    # Verify error for invalid inputs
    with pytest.raises(ValueError, match="Input must be at least 2"):
        generate_prime_sum_pairs(1)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        generate_prime_sum_pairs(0)
    
    with pytest.raises(ValueError, match="Input must be at least 2"):
        generate_prime_sum_pairs(-5)

def test_prime_sum_pairs_large_input():
    """Test prime sum pairs generation with a larger input."""
    result = generate_prime_sum_pairs(20)
    # Verify common potential prime sums
    possible_primes = {3, 5, 7, 11, 13}
    assert all(is_prime(x) for x in result)
    
    # Verify no non-prime sums
    for prime_sum in result:
        assert is_prime(prime_sum), f"{prime_sum} should be prime"