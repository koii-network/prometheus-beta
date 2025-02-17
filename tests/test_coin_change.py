import pytest
from src.coin_change import coin_change

def test_coin_change_basic_scenario():
    # Basic scenario with standard coins
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    
def test_coin_change_exact_match():
    # Scenario where exact coin matches amount
    assert coin_change([1, 2, 5], 5) == 1
    
def test_coin_change_impossible_amount():
    # Scenario where amount cannot be made with given coins
    assert coin_change([2], 3) == -1
    
def test_coin_change_zero_amount():
    # Edge case: zero amount
    assert coin_change([1, 2, 5], 0) == 0
    
def test_coin_change_large_amount():
    # Scenario with larger amount
    assert coin_change([1, 5, 10, 25], 100) == 4  # 25 + 25 + 25 + 25
    
def test_coin_change_multiple_solutions():
    # Scenario with multiple possible solutions, checking minimum
    assert coin_change([1, 3, 4], 6) == 2  # 3 + 3 or 4 + 1 + 1
    
def test_coin_change_no_coins():
    # Edge case: no coins available
    assert coin_change([], 5) == -1