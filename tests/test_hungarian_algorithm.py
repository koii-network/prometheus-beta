import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    # Simple 3x3 matrix
    cost_matrix = [
        [3, 2, 3],
        [1, 5, 4],
        [5, 2, 1]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    
    # Check assignment length
    assert len(assignments) == 3
    
    # Validate unique assignments
    assigned_rows = set(row for row, _ in assignments)
    assigned_cols = set(col for _, col in assignments)
    assert len(assigned_rows) == 3
    assert len(assigned_cols) == 3
    
    # Check total cost
    expected_assignments = [(0, 1), (1, 0), (2, 2)]
    assert set(assignments) == set(expected_assignments)
    assert total_cost == 4  # 2 + 1 + 1

def test_larger_matrix():
    # Larger 4x4 matrix
    cost_matrix = [
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    
    # Validate properties
    assert len(assignments) == 4
    assigned_rows = set(row for row, _ in assignments)
    assigned_cols = set(col for _, col in assignments)
    assert len(assigned_rows) == 4
    assert len(assigned_cols) == 4

def test_invalid_input():
    # Non-square matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([[1, 2], [3, 4], [5, 6]])
    
    # Empty matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([])

def test_symmetric_matrix():
    # Symmetric cost matrix
    cost_matrix = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    assert len(assignments) == 3
    assert total_cost <= 3  # Total should be minimal

def test_zero_matrix():
    # All zeros matrix
    cost_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    assert len(assignments) == 3
    assert total_cost == 0