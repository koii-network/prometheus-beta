import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value)
    max_weight = 10
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 13
    assert set(selected_items) == {1, 3}  # items at indices 1 and 3

def test_empty_items():
    """Test with empty items list"""
    items = []
    max_weight = 10
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_items == []

def test_zero_weight_capacity():
    """Test with zero weight capacity"""
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 0
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_items == []

def test_large_weight_capacity():
    """Test when weight capacity exceeds sum of all items"""
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 100
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 12
    assert set(selected_items) == {0, 1, 2}

def test_single_item():
    """Test with a single item that fits"""
    items = [(5, 10)]
    max_weight = 5
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 10
    assert selected_items == [0]

def test_single_item_too_heavy():
    """Test with a single item that's too heavy"""
    items = [(10, 5)]
    max_weight = 5
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_items == []