import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic():
    # Basic test case
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Cutting rod of length 4

def test_rod_cutting_zero_length():
    # Test with zero length rod
    prices = [1, 5, 8, 9]
    assert rod_cutting(prices, 0) == 0

def test_rod_cutting_single_length():
    # Test with single length rod
    prices = [3, 5, 8, 9]
    assert rod_cutting(prices, 1) == 3

def test_rod_cutting_empty_prices():
    # Test with empty prices list
    assert rod_cutting([], 5) == 0

def test_rod_cutting_longer_length():
    # Test with length longer than prices list
    prices = [1, 5, 8, 9, 10]
    assert rod_cutting(prices, 8) == 22  # Maximum possible value

def test_rod_cutting_max_value():
    # Test finding maximum possible value
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 8) == 24  # Verify max value