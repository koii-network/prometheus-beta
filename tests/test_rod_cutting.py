import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic_scenario():
    # Basic scenario with simple prices
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 4) == 10  # Best cut is 2 + 2 lengths

def test_rod_cutting_zero_length():
    # Test with zero length rod
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 0) == 0

def test_rod_cutting_single_length():
    # Test with single length rod for each possible price
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 1) == 1
    assert rod_cutting(prices, 2) == 5
    assert rod_cutting(prices, 3) == 8

def test_rod_cutting_longer_scenarios():
    # More complex scenarios
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    assert rod_cutting(prices, 7) == 20
    assert rod_cutting(prices, 8) == 22

def test_rod_cutting_insufficient_prices():
    # When prices list is shorter than rod length
    prices = [1, 5, 8]
    assert rod_cutting(prices, 4) == 10

def test_rod_cutting_invalid_inputs():
    # Test invalid input validation
    with pytest.raises(ValueError, match="Prices must be a list"):
        rod_cutting("not a list", 4)
    
    with pytest.raises(ValueError, match="Rod length must be a non-negative integer"):
        rod_cutting([1, 2, 3], -1)
    
    with pytest.raises(ValueError, match="Rod length must be a non-negative integer"):
        rod_cutting([1, 2, 3], "4")