import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    capacity = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_empty_knapsack():
    """Test when no items can be selected"""
    capacity = 5
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 0
    assert selected_items == []

def test_single_item_fits():
    """Test when a single item fits perfectly"""
    capacity = 10
    weights = [10]
    values = [100]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 100
    assert selected_items == [0]

def test_multiple_optimal_combinations():
    """Test when multiple combinations yield the same max value"""
    capacity = 10
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 7

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        solve_knapsack(10, [1, 2], [10, 20, 30])
    
    with pytest.raises(ValueError, match="Knapsack capacity must be non-negative"):
        solve_knapsack(-5, [1, 2], [10, 20])

def test_zero_weight_items():
    """Test scenario with zero-weight items"""
    capacity = 10
    weights = [0, 0, 5]
    values = [10, 20, 30]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 60
    assert set(selected_items) == {0, 1, 2}