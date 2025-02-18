import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm, is_valid_assignment

def test_basic_assignment():
    # Simple square matrix
    cost_matrix = [
        [3, 2, 3],
        [1, 5, 4],
        [2, 4, 6]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    # Validate assignment
    assert total_cost is not None
    assert len(assignment) == 3
    assert is_valid_assignment(cost_matrix, assignment)
    
    # Verify the assignment follows the minimum cost logic
    total_calculated_cost = sum(cost_matrix[worker][task] for worker, task in assignment)
    assert total_calculated_cost == total_cost

def test_rectangular_matrix_raises_error():
    # Rectangular matrix should raise ValueError
    cost_matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    with pytest.raises(ValueError, match="Cost matrix must be square"):
        hungarian_algorithm(cost_matrix)

def test_invalid_input_type():
    # Non-list/array input should raise ValueError
    invalid_inputs = [
        "not a matrix",
        123,
        None
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError, match="Input must be a 2D list or numpy array"):
            hungarian_algorithm(invalid_input)

def test_complex_assignment():
    # More complex cost matrix
    cost_matrix = [
        [7, 5, 3, 1],
        [2, 6, 4, 8],
        [5, 3, 9, 2],
        [4, 7, 6, 1]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost is not None
    assert len(assignment) == 4
    assert is_valid_assignment(cost_matrix, assignment)

def test_assignment_with_numpy_array():
    # Test with numpy array input
    cost_matrix = np.array([
        [3, 2, 3],
        [1, 5, 4],
        [2, 4, 6]
    ])
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost is not None
    assert len(assignment) == 3
    assert is_valid_assignment(cost_matrix, assignment)

def test_equal_cost_alternatives():
    # Matrix with multiple equivalent minimum cost assignments
    cost_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    total_cost, assignment = hungarian_algorithm(cost_matrix)
    
    assert total_cost == 3  # Each assignment costs 1
    assert len(assignment) == 3
    assert is_valid_assignment(cost_matrix, assignment)