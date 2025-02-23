import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_empty_items():
    """Test with empty items list"""
    assert solve_knapsack([], 10) == 0

def test_zero_capacity():
    """Test with zero capacity"""
    items = [(2, 3), (3, 4)]
    assert solve_knapsack(items, 0) == 0

def test_float_inputs():
    """Test with float inputs"""
    items = [(2.5, 3), (3.0, 4), (4.7, 5)]
    capacity = 10.5
    assert solve_knapsack(items, capacity) == 12

def test_invalid_capacity_negative():
    """Test with negative capacity"""
    items = [(2, 3), (3, 4)]
    with pytest.raises(ValueError, match="Capacity must be a non-negative number"):
        solve_knapsack(items, -1)

def test_invalid_item_input():
    """Test with invalid item input"""
    with pytest.raises(ValueError, match="Each item must be a tuple/list of"):
        solve_knapsack([(2, -3)], 10)
    
    with pytest.raises(ValueError, match="Each item must be a tuple/list of"):
        solve_knapsack(["invalid"], 10)

def test_complex_knapsack():
    """Test a more complex knapsack scenario"""
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    assert solve_knapsack(items, capacity) == 220

def test_edge_case_single_item():
    """Test with a single item that fits exactly"""
    items = [(10, 100)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 100

def test_edge_case_item_too_heavy():
    """Test when no items can fit in the knapsack"""
    items = [(15, 100), (20, 120)]
    capacity = 10
    assert solve_knapsack(items, capacity) == 0