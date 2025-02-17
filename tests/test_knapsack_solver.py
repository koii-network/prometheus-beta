import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_empty_knapsack():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 0
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 0
    assert selected_items == []

def test_single_item_fits():
    weights = [10]
    values = [60]
    capacity = 10
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 60
    assert selected_items == [0]

def test_mismatched_input_lengths():
    with pytest.raises(ValueError, match="Weights and values lists must have equal length"):
        solve_knapsack([10, 20], [60, 100, 120], 50)

def test_negative_capacity():
    with pytest.raises(ValueError, match="Knapsack capacity must be non-negative"):
        solve_knapsack([10, 20, 30], [60, 100, 120], -10)

def test_large_knapsack():
    weights = [1, 3, 4, 5]
    values = [10, 40, 50, 70]
    capacity = 10
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 160
    assert set(selected_items) == {1, 2, 3}