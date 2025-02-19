import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value)
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_empty_items():
    """Test with empty items list"""
    items = []
    capacity = 10
    assert solve_knapsack(items, capacity) == 0

def test_zero_capacity():
    """Test with zero capacity"""
    items = [(2, 3), (3, 4), (4, 5)]
    capacity = 0
    assert solve_knapsack(items, capacity) == 0

def test_negative_capacity():
    """Test with negative capacity"""
    items = [(2, 3), (3, 4), (4, 5)]
    capacity = -5
    assert solve_knapsack(items, capacity) == 0

def test_single_item_fits():
    """Test with a single item that fits in the knapsack"""
    items = [(5, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 10

def test_single_item_does_not_fit():
    """Test with a single item that does not fit in the knapsack"""
    items = [(6, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0

def test_complex_scenario():
    """Test a more complex knapsack scenario"""
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    assert solve_knapsack(items, capacity) == 220