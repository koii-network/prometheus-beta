import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic():
    # Basic test case
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Best way to cut a rod of length 4

def test_rod_cutting_single_length():
    # Test when rod length is 1
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 1

def test_rod_cutting_zero_length():
    # Test when rod length is 0
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_rod_cutting_full_length():
    # Test when using the entire rod length
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 8) == 22  # Optimal way to cut the rod

def test_rod_cutting_invalid_length():
    # Test when rod length exceeds price list
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    with pytest.raises(ValueError):
        rod_cutting(prices, 9)  # Prices list has only 8 elements

def test_rod_cutting_no_prices():
    # Test with an empty prices list
    with pytest.raises(ValueError):
        rod_cutting([], 3)