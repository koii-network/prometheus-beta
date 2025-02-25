import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_empty_items():
    """Test with empty items list"""
    assert solve_knapsack([], 10) == 0

def test_capacity_zero():
    """Test when capacity is zero"""
    items = [(2, 3), (3, 4)]
    assert solve_knapsack(items, 0) == 0

def test_exact_capacity():
    """Test when items exactly fit the capacity"""
    items = [(2, 3), (3, 4), (5, 6)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_insufficient_capacity():
    """Test when capacity is less than smallest item"""
    items = [(5, 10), (7, 15)]
    capacity = 3
    assert solve_knapsack(items, capacity) == 0

def test_float_inputs():
    """Test with float inputs"""
    items = [(2.5, 3.5), (3.7, 4.2)]
    capacity = 7.5
    assert solve_knapsack(items, capacity) == 7.7

def test_invalid_negative_capacity():
    """Test that negative capacity raises ValueError"""
    items = [(2, 3), (3, 4)]
    with pytest.raises(ValueError, match="Capacity must be a non-negative number"):
        solve_knapsack(items, -1)

def test_invalid_negative_weight():
    """Test that negative weight raises ValueError"""
    items = [(2, 3), (-3, 4)]
    with pytest.raises(ValueError, match="Item weights must be non-negative numbers"):
        solve_knapsack(items, 10)

def test_invalid_negative_value():
    """Test that negative value raises ValueError"""
    items = [(2, 3), (3, -4)]
    with pytest.raises(ValueError, match="Item values must be non-negative numbers"):
        solve_knapsack(items, 10)