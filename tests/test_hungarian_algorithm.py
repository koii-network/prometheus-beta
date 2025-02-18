import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    # Simple 3x3 matrix
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 5, 9]
    ]
    assignment = hungarian_algorithm(cost_matrix)
    
    # Verify assignment is correct length
    assert len(assignment) == 3
    
    # Verify each worker is assigned exactly once
    workers = [a[0] for a in assignment]
    assert len(set(workers)) == 3

def test_symmetric_matrix():
    # Perfectly symmetric matrix
    cost_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assignment = hungarian_algorithm(cost_matrix)
    
    # Any valid assignment is acceptable
    assert len(assignment) == 3

def test_invalid_matrix():
    # Non-square matrix should raise ValueError
    with pytest.raises(ValueError):
        hungarian_algorithm([
            [1, 2, 3],
            [4, 5, 6]
        ])

def test_complex_assignment():
    # More complex matrix
    cost_matrix = [
        [82, 83, 69, 92],
        [77, 37, 49, 92],
        [11, 69, 5, 86],
        [8, 9, 98, 23]
    ]
    assignment = hungarian_algorithm(cost_matrix)
    
    # Verify assignment properties
    assert len(assignment) == 4
    workers = [a[0] for a in assignment]
    tasks = [a[1] for a in assignment]
    assert len(set(workers)) == 4
    assert len(set(tasks)) == 4

def test_numpy_input():
    # Test with numpy array input
    cost_matrix = np.array([
        [1, 2, 3],
        [2, 4, 6],
        [3, 5, 9]
    ])
    assignment = hungarian_algorithm(cost_matrix)
    
    # Verify assignment is correct length
    assert len(assignment) == 3