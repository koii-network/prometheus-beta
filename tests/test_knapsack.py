import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    """Test a basic Knapsack problem scenario"""
    capacity = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_knapsack_with_no_items():
    """Test Knapsack with empty lists"""
    capacity = 10
    weights = []
    values = []
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    assert max_value == 0
    assert selected_items == []

def test_knapsack_with_insufficient_capacity():
    """Test Knapsack with capacity less than minimum item weight"""
    capacity = 5
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    assert max_value == 0
    assert selected_items == []

def test_mismatched_lists_raises_error():
    """Test that mismatched weights and values lists raise an error"""
    capacity = 50
    weights = [10, 20]
    values = [60, 100, 120]
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        solve_knapsack(capacity, weights, values)

def test_knapsack_complex_scenario():
    """Test a more complex Knapsack scenario"""
    capacity = 100
    weights = [10, 20, 30, 40]
    values = [60, 100, 120, 140]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    assert max_value == 260
    assert set(selected_items) == {0, 2, 3}