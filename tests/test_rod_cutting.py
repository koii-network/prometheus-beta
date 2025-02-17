import pytest
from src.rod_cutting import rod_cutting

def test_rod_cutting_basic():
    # Basic test case
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    max_value, cutting_strategy = rod_cutting(prices, 4)
    assert max_value == 10
    assert cutting_strategy in [[2, 2], [2, 1, 1]]

def test_rod_cutting_single_length():
    # Single length rod
    prices = [3]
    max_value, cutting_strategy = rod_cutting(prices, 1)
    assert max_value == 3
    assert cutting_strategy == [1]

def test_rod_cutting_empty_prices():
    # Empty prices list
    max_value, cutting_strategy = rod_cutting([], 5)
    assert max_value == 0
    assert cutting_strategy == []

def test_rod_cutting_zero_length():
    # Zero length rod
    prices = [1, 5, 8, 9, 10]
    max_value, cutting_strategy = rod_cutting(prices, 0)
    assert max_value == 0
    assert cutting_strategy == []

def test_rod_cutting_larger_n():
    # When n is larger than prices list
    prices = [1, 5, 8, 9, 10]
    max_value, cutting_strategy = rod_cutting(prices, 8)
    assert max_value > 0
    assert sum(cutting_strategy) == 8

def test_rod_cutting_no_cut_optimal():
    # Scenario where not cutting is optimal
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    max_value, cutting_strategy = rod_cutting(prices, 1)
    assert max_value == 1
    assert cutting_strategy == [1]