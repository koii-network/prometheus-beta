import pytest
from src.knapsack import solve_knapsack

def test_solve_knapsack_standard_case():
    """Test a standard knapsack problem scenario."""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value)
    capacity = 10
    assert solve_knapsack(items, capacity) == 13

def test_solve_knapsack_empty_items():
    """Test when no items are provided."""
    items = []
    capacity = 10
    assert solve_knapsack(items, capacity) == 0

def test_solve_knapsack_zero_capacity():
    """Test when knapsack capacity is zero."""
    items = [(2, 3), (3, 4), (4, 5)]
    capacity = 0
    assert solve_knapsack(items, capacity) == 0

def test_solve_knapsack_negative_capacity():
    """Test when knapsack capacity is negative."""
    items = [(2, 3), (3, 4), (4, 5)]
    capacity = -5
    assert solve_knapsack(items, capacity) == 0

def test_solve_knapsack_large_scenario():
    """Test a more complex knapsack scenario."""
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    assert solve_knapsack(items, capacity) == 220

def test_solve_knapsack_single_item():
    """Test with a single item that fits in capacity."""
    items = [(5, 10)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 10

def test_solve_knapsack_single_item_exceeds_capacity():
    """Test with a single item that exceeds capacity."""
    items = [(10, 50)]
    capacity = 5
    assert solve_knapsack(items, capacity) == 0