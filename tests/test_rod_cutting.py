import pytest
from src.rod_cutting import rod_cutting

def test_basic_rod_cutting():
    # Simple test case
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rod_length = 4
    max_revenue, cutting_strategy = rod_cutting(prices, rod_length)
    
    assert max_revenue == 10  # Either cut into two pieces of length 2
    assert set(cutting_strategy) == {2, 2}

def test_no_cutting():
    # When a single piece gives max revenue
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rod_length = 2
    max_revenue, cutting_strategy = rod_cutting(prices, rod_length)
    
    assert max_revenue == 5
    assert cutting_strategy == [2]

def test_empty_prices():
    # Edge case: empty prices list
    max_revenue, cutting_strategy = rod_cutting([], 5)
    
    assert max_revenue == 0
    assert cutting_strategy == []

def test_zero_length():
    # Edge case: zero rod length
    prices = [1, 5, 8, 9, 10]
    max_revenue, cutting_strategy = rod_cutting(prices, 0)
    
    assert max_revenue == 0
    assert cutting_strategy == []

def test_longer_rod_than_prices():
    # When rod length is longer than given prices
    prices = [1, 5, 8]
    rod_length = 5
    max_revenue, cutting_strategy = rod_cutting(prices, rod_length)
    
    assert max_revenue > 0  # Should still calculate a valid revenue
    assert sum(cutting_strategy) == rod_length

def test_maximum_revenue():
    # Comprehensive test for maximum revenue
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rod_length = 8
    max_revenue, cutting_strategy = rod_cutting(prices, rod_length)
    
    assert max_revenue == 40  # Selling entire rod of length 8
    assert cutting_strategy == [8]