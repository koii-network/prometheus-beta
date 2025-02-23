import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    # Basic test case
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    
def test_exact_match():
    # Test when a coin matches the exact amount
    assert min_coins([1, 2, 5], 5) == 1  # Single 5-coin
    
def test_multiple_coin_combinations():
    # Multiple ways to make change, should return minimum coins
    assert min_coins([1, 3, 4], 6) == 2  # 3 + 3 or 2 * 3
    
def test_impossible_amount():
    # Test when amount cannot be made exactly
    assert min_coins([2], 3) == -1
    
def test_zero_amount():
    # Test zero amount
    assert min_coins([1, 2, 5], 0) == 0
    
def test_large_amount():
    # Test a larger amount
    assert min_coins([1, 5, 10, 25], 100) == 4  # 4 * 25
    
def test_empty_coins():
    # Test with no coins available
    assert min_coins([], 5) == -1
    
def test_negative_amount():
    # Test negative amount
    assert min_coins([1, 2, 5], -1) == -1