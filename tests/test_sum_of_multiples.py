import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiples():
    """Test sum of multiples for 3 and 5"""
    assert sum_of_multiples(3, 5) == 60  # Multiples: 3, 5, 6, 9, 10, 12, 15, ...

def test_same_number():
    """Test when both inputs are the same"""
    assert sum_of_multiples(7, 7) == 28  # Multiples: 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98

def test_prime_numbers():
    """Test with prime numbers"""
    assert sum_of_multiples(2, 3) == 78  # Multiples: 2, 3, 4, 6, 8, 9, 10, 12, ...

def test_edge_cases():
    """Test edge cases of the input range"""
    assert sum_of_multiples(1, 1) == 5050  # Sum of all numbers from 1 to 100
    assert sum_of_multiples(100, 100) == 100

def test_invalid_input():
    """Test that invalid inputs raise ValueError"""
    with pytest.raises(ValueError):
        sum_of_multiples(0, 5)
    with pytest.raises(ValueError):
        sum_of_multiples(5, 101)
    with pytest.raises(ValueError):
        sum_of_multiples(-1, 10)