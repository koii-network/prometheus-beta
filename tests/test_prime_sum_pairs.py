import pytest
from src.prime_sum_pairs import generate_prime_sum_pairs, is_prime

def test_is_prime():
    """Test the is_prime helper function."""
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(15) == False

def test_generate_prime_sum_pairs_basic():
    """Test basic functionality of prime sum pairs generator."""
    result = generate_prime_sum_pairs(5)
    assert result == [5]

def test_generate_prime_sum_pairs_medium():
    """Test prime sum pairs for a medium input."""
    result = generate_prime_sum_pairs(10)
    assert result == [5, 7, 11, 13]

def test_generate_prime_sum_pairs_large():
    """Test prime sum pairs for a larger input."""
    result = generate_prime_sum_pairs(20)
    assert result == [5, 7, 11, 13, 17, 19, 23]

def test_generate_prime_sum_pairs_invalid_input():
    """Test invalid input handling."""
    with pytest.raises(TypeError):
        generate_prime_sum_pairs("10")
    
    with pytest.raises(ValueError):
        generate_prime_sum_pairs(1)

def test_generate_prime_sum_pairs_unique():
    """Ensure returned prime sums are unique and sorted."""
    result = generate_prime_sum_pairs(10)
    assert len(result) == len(set(result))
    assert result == sorted(result)