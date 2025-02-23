import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    capacity = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_empty_input():
    """Test with empty lists"""
    capacity = 10
    weights = []
    values = []
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 0
    assert selected_items == []

def test_zero_capacity():
    """Test with zero knapsack capacity"""
    capacity = 0
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 0
    assert selected_items == []

def test_single_item_fits():
    """Test with a single item that fits in the knapsack"""
    capacity = 10
    weights = [5]
    values = [50]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 50
    assert selected_items == [0]

def test_single_item_does_not_fit():
    """Test with a single item that does not fit in the knapsack"""
    capacity = 5
    weights = [10]
    values = [50]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 0
    assert selected_items == []

def test_multiple_optimal_solutions():
    """Test a scenario with multiple ways to achieve the same max value"""
    capacity = 10
    weights = [5, 5, 5]
    values = [10, 10, 10]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 20
    assert len(selected_items) == 2

def test_mismatched_input_lengths():
    """Test that ValueError is raised for mismatched input lists"""
    capacity = 50
    weights = [10, 20]
    values = [60, 100, 120]
    
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        solve_knapsack(capacity, weights, values)

def test_negative_capacity():
    """Test that ValueError is raised for negative capacity"""
    capacity = -10
    weights = [10, 20, 30]
    values = [60, 100, 120]
    
    with pytest.raises(ValueError, match="Knapsack capacity must be non-negative"):
        solve_knapsack(capacity, weights, values)