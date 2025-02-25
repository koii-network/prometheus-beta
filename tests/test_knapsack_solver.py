import pytest
from src.knapsack_solver import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    items = [(2, 3), (3, 4), (4, 5), (5, 6)]
    max_weight = 10
    result = solve_knapsack(items, max_weight)
    
    # Validate result
    total_weight = sum(item[0] for item in result)
    total_value = sum(item[1] for item in result)
    
    assert total_weight <= max_weight
    assert total_value == 13  # Optimal solution: (3,4) and (4,5)
    assert len(result) <= len(items)

def test_empty_items():
    """Test with no items"""
    items = []
    max_weight = 10
    result = solve_knapsack(items, max_weight)
    
    assert result == []

def test_zero_capacity():
    """Test with zero weight capacity"""
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 0
    result = solve_knapsack(items, max_weight)
    
    assert result == []

def test_negative_weight_error():
    """Test error handling for negative weight"""
    items = [(2, 3), (3, 4)]
    
    with pytest.raises(ValueError, match="Maximum weight must be non-negative"):
        solve_knapsack(items, -1)

def test_negative_item_weight_error():
    """Test error handling for negative item weight"""
    items = [(2, 3), (-1, 4)]
    
    with pytest.raises(ValueError, match="Item weights and values must be non-negative"):
        solve_knapsack(items, 10)

def test_large_capacity():
    """Test with capacity larger than total item weights"""
    items = [(2, 3), (3, 4), (4, 5)]
    max_weight = 100
    result = solve_knapsack(items, max_weight)
    
    total_weight = sum(item[0] for item in result)
    total_value = sum(item[1] for item in result)
    
    assert total_value == 12  # Total value of all items
    assert total_weight <= max_weight

def test_item_selection():
    """Detailed test of specific item selection"""
    items = [(10, 60), (20, 100), (30, 120)]
    max_weight = 50
    result = solve_knapsack(items, max_weight)
    
    # Expected result: (20, 100) and (30, 120)
    expected_result = [(20, 100), (30, 120)]
    
    assert set(result) == set(expected_result)
    assert sum(item[0] for item in result) <= max_weight