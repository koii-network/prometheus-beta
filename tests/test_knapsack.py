import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [
        {'weight': 2, 'value': 3},
        {'weight': 3, 'value': 4},
        {'weight': 4, 'value': 5}
    ]
    capacity = 6
    assert solve_knapsack(items, capacity) == 7

def test_empty_items():
    """Test with an empty list of items"""
    assert solve_knapsack([], 10) == 0

def test_zero_capacity():
    """Test with zero capacity"""
    items = [
        {'weight': 2, 'value': 3},
        {'weight': 3, 'value': 4}
    ]
    assert solve_knapsack(items, 0) == 0

def test_items_exceed_capacity():
    """Test when all items are too heavy"""
    items = [
        {'weight': 10, 'value': 5},
        {'weight': 20, 'value': 10}
    ]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0

def test_invalid_items_input():
    """Test invalid items input"""
    with pytest.raises(ValueError, match="Items must be a list of dictionaries"):
        solve_knapsack("not a list", 10)

def test_invalid_capacity():
    """Test invalid capacity input"""
    items = [{'weight': 2, 'value': 3}]
    
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack(items, -1)
    
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack(items, "not an integer")

def test_complex_knapsack():
    """Test a more complex knapsack scenario"""
    items = [
        {'weight': 1, 'value': 1},
        {'weight': 3, 'value': 4},
        {'weight': 4, 'value': 5},
        {'weight': 5, 'value': 7}
    ]
    capacity = 10
    assert solve_knapsack(items, capacity) == 12