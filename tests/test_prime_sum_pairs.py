import pytest
from src.prime_sum_pairs import generate_prime_sum_pairs, is_prime

def test_is_prime():
    """Test the is_prime helper function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False

def test_generate_prime_sum_pairs_basic():
    """Test basic functionality of generate_prime_sum_pairs."""
    # For n=4, possible pairs are:
    # 1+1=2(prime), 1+2=3(prime), 1+3=4(not prime), 1+4=5(prime)
    # 2+2=4(not prime), 2+3=5(prime), 2+4=6(not prime)
    # 3+3=6(not prime), 3+4=7(prime)
    # 4+4=8(not prime)
    assert generate_prime_sum_pairs(4) == [2, 3, 5, 7]

def test_generate_prime_sum_pairs_edge_cases():
    """Test edge cases for generate_prime_sum_pairs."""
    # Smallest valid input
    assert generate_prime_sum_pairs(1) == []
    
    # Slightly larger input
    result = generate_prime_sum_pairs(10)
    assert all(is_prime(num) for num in result)
    assert result == sorted(set(result))

def test_generate_prime_sum_pairs_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        generate_prime_sum_pairs(0)
    
    with pytest.raises(ValueError):
        generate_prime_sum_pairs(-5)
    
    with pytest.raises(ValueError):
        generate_prime_sum_pairs(3.14)
    
    with pytest.raises(ValueError):
        generate_prime_sum_pairs("not a number")

def test_generate_prime_sum_pairs_larger_input():
    """Test with a larger input to ensure performance and correctness."""
    result = generate_prime_sum_pairs(20)
    assert all(is_prime(num) for num in result)
    assert result == sorted(set(result))
    # Verify some known prime sums
    assert 5 in result   # 1+4
    assert 7 in result   # 3+4
    assert 11 in result  # 4+7
    assert 13 in result  # 4+9
    assert 17 in result  # 5+12