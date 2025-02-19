import pytest
from src.prime_sum import sum_primes_under_n

def test_sum_primes_under_10():
    """Test sum of primes less than 10"""
    assert sum_primes_under_n(10) == 17  # 2 + 3 + 5 + 7

def test_sum_primes_under_2():
    """Test input less than 2 returns 0"""
    assert sum_primes_under_n(2) == 0

def test_sum_primes_under_1():
    """Test input of 1 returns 0"""
    assert sum_primes_under_n(1) == 0

def test_sum_primes_large_number():
    """Test a larger number"""
    assert sum_primes_under_n(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19

def test_invalid_input_float():
    """Test float input raises TypeError"""
    with pytest.raises(TypeError):
        sum_primes_under_n(10.5)

def test_invalid_input_string():
    """Test string input raises TypeError"""
    with pytest.raises(TypeError):
        sum_primes_under_n("10")

def test_invalid_input_negative():
    """Test negative input"""
    assert sum_primes_under_n(-5) == 0