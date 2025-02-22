import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    # Basic scenario with multiple items
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 13  # Best combination

def test_empty_items():
    # Empty list of items should return 0
    assert solve_knapsack([], 10) == 0

def test_zero_capacity():
    # No items can be added when capacity is 0
    items = [(2, 3), (3, 4)]
    assert solve_knapsack(items, 0) == 0

def test_single_item_fits():
    # Single item that fits exactly
    items = [(5, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 10

def test_single_item_does_not_fit():
    # Single item that doesn't fit
    items = [(6, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0

def test_multiple_combinations():
    # Complex scenario with multiple possible combinations
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    assert solve_knapsack(items, capacity) == 220

def test_invalid_negative_capacity():
    # Negative capacity should raise ValueError
    items = [(2, 3), (3, 4)]
    with pytest.raises(ValueError, match="Knapsack capacity must be non-negative"):
        solve_knapsack(items, -1)

def test_invalid_negative_item_weight():
    # Negative item weight should raise ValueError
    items = [(2, 3), (-3, 4)]
    with pytest.raises(ValueError, match="Item weights and values must be non-negative"):
        solve_knapsack(items, 10)

def test_invalid_negative_item_value():
    # Negative item value should raise ValueError
    items = [(2, 3), (3, -4)]
    with pytest.raises(ValueError, match="Item weights and values must be non-negative"):
        solve_knapsack(items, 10)