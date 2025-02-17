import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic():
    """Test basic rod cutting scenario"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    max_value, cuts = rod_cutting(prices, 4)
    assert max_value == 10
    assert cuts == [2, 2]  # two pieces of length 2

def test_rod_cutting_full_length():
    """Test when cutting the entire rod in one piece"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    max_value, cuts = rod_cutting(prices, 8)
    assert max_value == 20
    assert cuts == [8]

def test_rod_cutting_empty_prices():
    """Test with empty prices list"""
    max_value, cuts = rod_cutting([], 5)
    assert max_value == 0
    assert cuts == []

def test_rod_cutting_zero_length():
    """Test with rod length of zero"""
    prices = [1, 5, 8, 9, 10]
    max_value, cuts = rod_cutting(prices, 0)
    assert max_value == 0
    assert cuts == []

def test_rod_cutting_different_lengths():
    """Test with prices for different rod lengths"""
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    max_value, cuts = rod_cutting(prices, 5)
    assert max_value == 13  # max value can be obtained by cutting
    assert len(cuts) > 0

def test_rod_cutting_longer_rod():
    """Test when rod length is longer than prices list"""
    prices = [1, 5, 8]
    max_value, cuts = rod_cutting(prices, 5)
    assert max_value > 0
    assert len(cuts) > 0