import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    # Basic test cases
    assert min_coins(11, [1, 2, 5]) == 3  # 5 + 5 + 1
    assert min_coins(4, [1, 2, 5]) == 2   # 2 + 2
    assert min_coins(6, [1, 3, 4]) == 2   # 3 + 3 or 2 + 4

def test_exact_match():
    # Exact match of single coin
    assert min_coins(5, [1, 2, 5]) == 1
    assert min_coins(2, [1, 2, 5]) == 1

def test_impossible_change():
    # Impossible to make change
    assert min_coins(3, [2, 4]) == -1
    assert min_coins(7, [3, 5]) == -1

def test_zero_amount():
    # Edge case: zero amount
    assert min_coins(0, [1, 2, 5]) == 0

def test_large_number():
    # Larger amount test
    assert min_coins(100, [1, 5, 10, 25]) == 4  # 4 x 25

def test_no_coins():
    # No coins available
    assert min_coins(5, []) == -1

def test_negative_amount():
    # Negative amount
    assert min_coins(-5, [1, 2, 5]) == -1