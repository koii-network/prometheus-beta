import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack problem with a few items."""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value)
    max_weight = 10
    max_value, selected_indices = solve_knapsack(items, max_weight)
    
    # Verify the result
    assert max_value == 13
    assert set(selected_indices) == {1, 2}  # items at indices 1 and 2
    
    # Verify the selected items match the expected total weight and value
    selected_items = [items[i] for i in selected_indices]
    assert sum(item[0] for item in selected_items) <= max_weight
    assert sum(item[1] for item in selected_items) == max_value

def test_empty_items():
    """Test with an empty list of items."""
    items = []
    max_weight = 10
    max_value, selected_indices = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_indices == []

def test_zero_weight_capacity():
    """Test with zero weight capacity."""
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 0
    max_value, selected_indices = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_indices == []

def test_single_item():
    """Test with a single item that fits in the knapsack."""
    items = [(5, 10)]
    max_weight = 5
    max_value, selected_indices = solve_knapsack(items, max_weight)
    
    assert max_value == 10
    assert selected_indices == [0]

def test_no_items_fit():
    """Test when no items can fit in the knapsack."""
    items = [(10, 5), (15, 8)]
    max_weight = 5
    max_value, selected_indices = solve_knapsack(items, max_weight)
    
    assert max_value == 0
    assert selected_indices == []

def test_multiple_optimal_solutions():
    """Test a scenario with multiple ways to achieve the same max value."""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    max_weight = 10
    max_value, selected_indices = solve_knapsack(items, max_weight)
    
    assert max_value == 13
    assert set(selected_indices).issubset({1, 2})  # can be different valid combinations

def test_large_input():
    """Test with a larger number of items."""
    items = [(1, 1), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
    max_weight = 15
    max_value, selected_indices = solve_knapsack(items, max_weight)
    
    assert max_value > 0
    assert sum(items[i][0] for i in selected_indices) <= max_weight