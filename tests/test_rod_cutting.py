import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic():
    # Basic test case
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Best way to cut rod of length 4

def test_rod_cutting_full_length():
    # Test cutting the entire rod at its original length
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 8) == 20  # Best value for full length rod

def test_rod_cutting_single_length():
    # Test for a single length rod
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 3  # Price of first length

def test_rod_cutting_empty_prices():
    # Edge case: empty prices list
    prices = []
    assert rod_cutting(prices, 4) == 0  # No prices, so max value is 0

def test_rod_cutting_long_rod():
    # Test scenario where rod is longer than available prices
    prices = [1, 5, 8]
    assert rod_cutting(prices, 5) == 11  # Combination of available prices