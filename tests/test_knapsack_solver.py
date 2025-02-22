import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    # Basic test case
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    max_weight = 10
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 13
    assert set(selected) == {1, 3}  # items at indices 1 and 3

def test_empty_items():
    # Empty items list
    items = []
    max_weight = 10
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 0
    assert selected == []

def test_zero_weight_capacity():
    # No weight capacity
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 0
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 0
    assert selected == []

def test_negative_weight_capacity():
    # Negative weight capacity
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = -5
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 0
    assert selected == []

def test_single_item_fits():
    # Single item that fits exactly
    items = [(5, 10)]
    max_weight = 5
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 10
    assert selected == [0]

def test_single_item_too_heavy():
    # Single item that is too heavy
    items = [(10, 10)]
    max_weight = 5
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 0
    assert selected == []

def test_multiple_optimal_solutions():
    # Multiple ways to achieve same max value
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 7
    max_value, selected = solve_knapsack(items, max_weight)
    assert max_value == 9
    # Either [1, 2] or [0, 1] could be valid
    assert (selected == [1, 2]) or (selected == [0, 1])