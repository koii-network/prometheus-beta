import pytest
from src.coin_change import coin_change

def test_standard_case():
    """Test typical case with multiple coin denominations"""
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3  # 5 + 5 + 1

def test_exact_coin_match():
    """Test when exact coin denomination exists"""
    coins = [1, 2, 5]
    amount = 5
    assert coin_change(coins, amount) == 1

def test_impossible_amount():
    """Test when amount cannot be made with given coins"""
    coins = [2]
    amount = 3
    assert coin_change(coins, amount) == -1

def test_zero_amount():
    """Test case with zero amount"""
    coins = [1, 2, 5]
    amount = 0
    assert coin_change(coins, amount) == 0

def test_large_amount():
    """Test with a larger amount"""
    coins = [1, 5, 10, 25]
    amount = 100
    assert coin_change(coins, amount) == 4  # 25 + 25 + 25 + 25

def test_empty_coins():
    """Test with empty coins list"""
    coins = []
    amount = 5
    assert coin_change(coins, amount) == -1