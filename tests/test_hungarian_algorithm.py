import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    # Simple square matrix
    cost_matrix = [
        [3, 2, 3],
        [3, 3, 3],
        [3, 3, 3]
    ]
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    # Verify assignment length matches matrix size
    assert len(assignment) == 3
    
    # Verify each row and column used only once
    rows, cols = zip(*assignment)
    assert len(set(rows)) == 3
    assert len(set(cols)) == 3

def test_numpy_input():
    # Test with numpy array input
    cost_matrix = np.array([
        [5, 4, 3],
        [2, 7, 6],
        [6, 3, 4]
    ])
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    # Verify assignment length matches matrix size
    assert len(assignment) == 3

def test_minimal_cost():
    # Matrix where goal is to minimize total assignment cost
    cost_matrix = [
        [7, 5, 3],
        [2, 4, 6],
        [4, 7, 8]
    ]
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    # Verify total cost is minimal
    expected_assignment = [(0, 2), (1, 0), (2, 1)]
    assert sorted(assignment) == expected_assignment

def test_invalid_input():
    # Test non-square matrix
    with pytest.raises(ValueError, match="Cost matrix must be a square matrix"):
        hungarian_algorithm([
            [1, 2, 3],
            [4, 5, 6]
        ])
    
    # Test non-list/array input
    with pytest.raises(ValueError, match="Input must be a 2D list or numpy array"):
        hungarian_algorithm("not a matrix")

def test_large_matrix():
    # Test with a larger matrix
    cost_matrix = np.random.randint(1, 100, (5, 5))
    assignment, total_cost = hungarian_algorithm(cost_matrix)
    
    # Verify assignment length matches matrix size
    assert len(assignment) == 5
    
    # Verify each row and column used only once
    rows, cols = zip(*assignment)
    assert len(set(rows)) == 5
    assert len(set(cols)) == 5