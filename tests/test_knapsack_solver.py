import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    # Basic scenario with a few items
    items = [(10, 60), (20, 100), (30, 120)]
    max_weight = 50
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_empty_items():
    # Test with no items
    items = []
    max_weight = 100
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_items == []

def test_max_weight_zero():
    # Test with zero max weight
    items = [(10, 60), (20, 100), (30, 120)]
    max_weight = 0
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_items == []

def test_single_item_fits():
    # Test with a single item that fits
    items = [(10, 100)]
    max_weight = 10
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 100
    assert selected_items == [0]

def test_single_item_does_not_fit():
    # Test with a single item that does not fit
    items = [(10, 100)]
    max_weight = 5
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_items == []

def test_complex_scenario():
    # A more complex scenario with multiple items
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    max_weight = 10
    max_value, selected_items = solve_knapsack(items, max_weight)
    
    assert max_value == 15
    assert set(selected_items) == {1, 2, 3}