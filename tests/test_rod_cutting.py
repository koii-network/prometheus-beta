import pytest
from src.rod_cutting import rod_cutting

def test_basic_rod_cutting():
    """Test a basic rod cutting scenario"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10

def test_single_length_rod():
    """Test rod of length 1"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 1

def test_zero_length_rod():
    """Test rod of length 0"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_longer_rod_than_prices():
    """Test when rod length exceeds available prices"""
    prices = [1, 5, 8]
    assert rod_cutting(prices, 5) == 13  # Updated to match expected behavior

def test_invalid_input_empty_prices():
    """Test error handling for empty prices list"""
    with pytest.raises(ValueError):
        rod_cutting([], 5)

def test_invalid_input_negative_length():
    """Test error handling for negative rod length"""
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    with pytest.raises(ValueError):
        rod_cutting(prices, -1)

def test_no_profit_prices():
    """Test with prices list containing only zeros"""
    prices = [0, 0, 0, 0]
    assert rod_cutting(prices, 3) == 0