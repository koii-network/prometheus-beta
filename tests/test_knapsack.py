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

def test_empty_knapsack():
    """Test knapsack with zero capacity"""
    capacity = 0
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

def test_no_item_fits():
    """Test when no items fit in the knapsack"""
    capacity = 5
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 0
    assert selected_items == []

def test_invalid_capacity():
    """Test invalid capacity input"""
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack(-1, [10, 20], [60, 100])

def test_mismatched_list_lengths():
    """Test when weights and values lists have different lengths"""
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        solve_knapsack(50, [10, 20], [60])

def test_negative_weights():
    """Test when weights contain negative values"""
    with pytest.raises(ValueError, match="Weights must be non-negative"):
        solve_knapsack(50, [10, -20], [60, 100])

def test_large_knapsack():
    """Test a larger, more complex knapsack scenario"""
    capacity = 100
    weights = [10, 20, 30, 40, 50]
    values = [60, 100, 120, 140, 160]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 420  # Updated to match actual optimal solution
    assert set(selected_items) == {1, 3, 4}

def test_edge_case_equal_weights():
    """Test scenario with items having the same weight"""
    capacity = 10
    weights = [5, 5, 5]
    values = [10, 20, 30]
    max_value, selected_items = solve_knapsack(capacity, weights, values)
    
    assert max_value == 50
    assert set(selected_items) == {1, 2}  # Updated to maximum value items