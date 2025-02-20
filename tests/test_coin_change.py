import pytest
from src.coin_change import min_coins

def test_simple_coin_change():
    coins = [1, 2, 5]
    amount = 11
    assert min_coins(coins, amount) == 3  # 5 + 5 + 1

def test_exact_single_coin():
    coins = [1, 2, 5]
    amount = 5
    assert min_coins(coins, amount) == 1  # single 5-coin

def test_impossible_change():
    coins = [2]
    amount = 3
    assert min_coins(coins, amount) == -1  # cannot make 3 with only 2-coin

def test_zero_amount():
    coins = [1, 2, 5]
    amount = 0
    assert min_coins(coins, amount) == 0  # 0 coins needed for 0 amount

def test_large_denomination():
    coins = [186, 419, 83, 408]
    amount = 6249
    assert min_coins(coins, amount) == 20  # complex large amount case

def test_multiple_coin_combinations():
    coins = [1, 3, 4]
    amount = 6
    assert min_coins(coins, amount) == 2  # 3 + 3 or 4 + 2

def test_empty_coins_list():
    coins = []
    amount = 5
    assert min_coins(coins, amount) == -1  # no coins provided