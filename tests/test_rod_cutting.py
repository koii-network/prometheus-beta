import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic():
    """Test basic rod cutting scenario"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10

def test_rod_cutting_single_piece():
    """Test when rod length is 1"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 1

def test_rod_cutting_zero_length():
    """Test with zero length rod"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_rod_cutting_empty_prices():
    """Test with empty prices list"""
    assert rod_cutting([], 5) == 0

def test_rod_cutting_longer_rod():
    """Test when rod length is longer than prices list"""
    prices = [1, 5, 8, 9, 10]
    assert rod_cutting(prices, 8) > 0

def test_rod_cutting_optimal_splitting():
    """Test a more complex scenario with optimal splitting"""
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 11  # Splitting into two pieces of length 2