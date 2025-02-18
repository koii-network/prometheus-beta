import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_simple_assignment():
    # Simple square matrix
    cost_matrix = [
        [3, 4, 1],
        [2, 1, 5],
        [3, 2, 4]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    # Verify total cost and assignment
    assert total_cost == 5  # Actual optimal assignment cost
    assert set(assignment) == {(0, 2), (1, 1), (2, 0)}

def test_rectangular_matrix():
    # Rectangular matrix (more workers than jobs)
    cost_matrix = [
        [3, 2, 1],
        [1, 4, 2],
        [5, 3, 6],
        [4, 1, 5]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    # Verify assignment length
    assert len(assignment) == 3  # Number of jobs
    assert total_cost is not None

def test_zero_cost_matrix():
    # All zeros matrix
    cost_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 0
    assert len(assignment) == 3

def test_single_element_matrix():
    # Single element matrix
    cost_matrix = [[5]]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 5
    assert assignment == [(0, 0)]

def test_invalid_input():
    # Test invalid input types
    with pytest.raises(ValueError):
        hungarian_algorithm([1, 2, 3])  # 1D list
    
    with pytest.raises(ValueError):
        hungarian_algorithm(np.array([1, 2, 3]))  # 1D array

def test_large_matrix():
    # Larger matrix to test scalability
    np.random.seed(42)
    cost_matrix = np.random.randint(1, 100, size=(5, 5))
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert len(assignment) == 5
    assert total_cost is not None
    
    # Verify each worker and job is assigned exactly once
    workers, jobs = zip(*assignment)
    assert len(set(workers)) == len(workers)
    assert len(set(jobs)) == len(jobs)