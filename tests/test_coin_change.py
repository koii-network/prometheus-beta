import pytest
from src.coin_change import coin_change

def test_basic_coin_change():
    # Basic scenario with standard coins
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change([2], 3) == -1  # Cannot make 3 with only 2-coin

def test_single_coin_denomination():
    # Test with a single coin denomination
    assert coin_change([1], 5) == 5  # Need 5 one-cent coins
    assert coin_change([5], 10) == 2  # Need 2 five-cent coins

def test_zero_amount():
    # Amount of zero should always return 0
    assert coin_change([1, 2, 5], 0) == 0

def test_large_amount():
    # Test with larger amount and multiple coin denominations
    assert coin_change([1, 5, 10, 25], 67) == 5  # 25 + 25 + 10 + 5 + 2

def test_impossible_change():
    # Scenarios where change cannot be made
    assert coin_change([2], 7) == -1
    assert coin_change([5], 3) == -1

def test_edge_cases():
    # Negative amounts or empty coin list
    assert coin_change([], 5) == -1
    assert coin_change([1, 2, 5], -1) == -1

def test_greedy_algorithm_failure():
    # Test a case where greedy approach fails
    assert coin_change([1, 3, 4], 6) == 2  # Need 3 + 3, not 4 + 1 + 1