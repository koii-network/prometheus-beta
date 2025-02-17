import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic():
    # Basic test case
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Should choose two pieces of length 2

def test_rod_cutting_zero_length():
    # Test zero-length rod
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_rod_cutting_single_length():
    # Test single length rod
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 1

def test_rod_cutting_long_rod():
    # Test a longer rod
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 8) == 40

def test_rod_cutting_with_short_price_list():
    # Test when price list is shorter than rod length
    prices = [0, 3, 5]
    assert rod_cutting(prices, 5) == 15

def test_rod_cutting_empty_prices():
    # Test with empty prices list
    assert rod_cutting([], 5) == 0