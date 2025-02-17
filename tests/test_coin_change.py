import pytest
from src.coin_change import coin_change

def test_coin_change_basic_scenario():
    # Standard case with multiple coin denominations
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3  # 5 + 5 + 1

def test_coin_change_exact_amount():
    # Exact amount with single coin
    coins = [1, 2, 5]
    amount = 5
    assert coin_change(coins, amount) == 1  # Single 5-coin

def test_coin_change_impossible_amount():
    # Amount that cannot be made
    coins = [2]
    amount = 3
    assert coin_change(coins, amount) == -1

def test_coin_change_zero_amount():
    # Zero amount case
    coins = [1, 2, 5]
    amount = 0
    assert coin_change(coins, amount) == 0

def test_coin_change_large_amount():
    # Large amount with multiple coin denominations
    coins = [1, 5, 10, 25]
    amount = 100
    assert coin_change(coins, amount) == 4  # 25 + 25 + 25 + 25

def test_coin_change_no_coins():
    # No coins available
    coins = []
    amount = 5
    assert coin_change(coins, amount) == -1

def test_coin_change_large_denominations():
    # Large coin denominations
    coins = [186, 419, 83, 408]
    amount = 6249
    assert coin_change(coins, amount) == 20