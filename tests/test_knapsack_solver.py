import pytest
from src.knapsack_solver import solve_knapsack

def test_standard_knapsack_case():
    """Test a standard knapsack problem scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 13.0

def test_empty_items_list():
    """Test with an empty list of items"""
    assert solve_knapsack([], 10) == 0.0

def test_zero_capacity():
    """Test with zero knapsack capacity"""
    items = [(2, 3), (3, 4)]
    assert solve_knapsack(items, 0) == 0.0

def test_single_item_fits():
    """Test when a single item fits perfectly"""
    items = [(5, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 10.0

def test_single_item_does_not_fit():
    """Test when a single item does not fit"""
    items = [(6, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0.0

def test_multiple_same_weight_items():
    """Test multiple items with same weight"""
    items = [(2, 3), (2, 4), (2, 5)]
    capacity = 4
    assert solve_knapsack(items, capacity) == 9.0

def test_invalid_items_type():
    """Test invalid items input (not a list)"""
    with pytest.raises(ValueError, match="Items must be a list"):
        solve_knapsack("not a list", 10)

def test_invalid_capacity_type():
    """Test invalid capacity input"""
    items = [(2, 3), (3, 4)]
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack(items, -1)
    
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack(items, "invalid")

def test_invalid_item_format():
    """Test invalid item tuples"""
    items = [(2, 3), "invalid", (4, 5)]
    with pytest.raises(ValueError, match="Each item must be a tuple"):
        solve_knapsack(items, 10)

def test_large_input():
    """Test with a larger number of items"""
    items = [(10, 20), (20, 30), (30, 40), (40, 50), (50, 60)]
    capacity = 100
    assert solve_knapsack(items, capacity) == 140.0

def test_floating_point_weights():
    """Test with floating-point weights and values"""
    items = [(2.5, 3.5), (3.5, 4.5), (4.5, 5.5)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 10.0  # Correct result based on knapsack constraint