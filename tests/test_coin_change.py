import pytest
from src.coin_change import coin_change

def test_standard_case():
    # Basic case with multiple coins
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1

def test_exact_match():
    # Test when exact match is possible
    assert coin_change([1, 2, 5], 5) == 1  # Single 5-coin

def test_impossible_amount():
    # Test when amount cannot be made
    assert coin_change([2], 3) == -1

def test_single_coin_multiple_times():
    # Test when multiple coins of same denomination are used
    assert coin_change([1], 5) == 5  # 5 one-cent coins

def test_large_amount():
    # Test with a larger amount
    assert coin_change([1, 5, 10, 25], 99) == 9  # Multiple coin combination

def test_zero_amount():
    # Test when amount is zero
    assert coin_change([1, 2, 5], 0) == 0

def test_empty_coins():
    # Test with no coins available
    assert coin_change([], 5) == -1