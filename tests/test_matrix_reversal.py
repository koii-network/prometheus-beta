import pytest
from src.matrix_reversal import reverse_matrix_elements

def test_reverse_matrix_elements_basic():
    """Test basic matrix element reversal."""
    matrix = [
        [12, 34],
        [56, 78]
    ]
    expected = [
        [21, 43],
        [65, 87]
    ]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_single_digit():
    """Test matrix with single-digit elements."""
    matrix = [
        [1, 2],
        [3, 4]
    ]
    expected = [
        [1, 2],
        [3, 4]
    ]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_single_element():
    """Test a single-element matrix."""
    matrix = [[5]]
    expected = [[5]]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_zeros():
    """Test matrix with zero elements."""
    matrix = [
        [0, 0],
        [0, 0]
    ]
    expected = [
        [0, 0],
        [0, 0]
    ]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_leading_zeros():
    """Test matrix with elements that simulate leading zeros."""
    matrix = [
        [1, 2],
        [3, 4]
    ]
    expected = [
        [1, 2],
        [3, 4]
    ]
    assert reverse_matrix_elements(matrix) == expected

def test_invalid_matrix_non_square():
    """Test that a non-square matrix raises an error."""
    matrix = [
        [1, 2, 3],
        [4, 5]
    ]
    with pytest.raises(ValueError, match="Matrix must be square"):
        reverse_matrix_elements(matrix)

def test_invalid_matrix_empty():
    """Test that an empty matrix raises an error."""
    matrix = []
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        reverse_matrix_elements(matrix)

def test_invalid_matrix_out_of_range():
    """Test that a matrix with large multi-digit numbers works correctly."""
    matrix = [
        [10, 100],
        [1000, 50]
    ]
    expected = [
        [1, 1],
        [0, 5]
    ]
    assert reverse_matrix_elements(matrix) == expected

def test_matrix_size_constraints():
    """Test matrix size constraints."""
    # This test assumes you want to limit matrix size to 1-1000
    # Test too small
    matrix = []
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        reverse_matrix_elements(matrix)

    # Test too large
    import numpy as np
    large_matrix = np.ones((1001, 1001), dtype=int).tolist()
    with pytest.raises(ValueError, match="Matrix size must be between 1 and 1000"):
        reverse_matrix_elements(large_matrix)