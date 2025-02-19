import pytest
from src.matrix_element_reverser import reverse_matrix_elements

def test_reverse_matrix_elements_basic():
    """Test basic matrix element reversal"""
    input_matrix = [
        [1, 23, 4],
        [56, 7, 89],
        [0, 12, 345]
    ]
    expected_matrix = [
        [1, 32, 4],
        [65, 7, 98],
        [0, 21, 543]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix

def test_reverse_matrix_elements_single_digit():
    """Test matrix with single-digit elements"""
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert reverse_matrix_elements(input_matrix) == input_matrix

def test_reverse_matrix_elements_zero_elements():
    """Test matrix with zero elements"""
    input_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert reverse_matrix_elements(input_matrix) == input_matrix

def test_reverse_matrix_single_element():
    """Test single-element matrix"""
    input_matrix = [[5]]
    assert reverse_matrix_elements(input_matrix) == [[5]]

def test_matrix_empty_raises_error():
    """Test that empty matrix raises ValueError"""
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        reverse_matrix_elements([])

def test_non_square_matrix_raises_error():
    """Test that non-square matrix raises ValueError"""
    with pytest.raises(ValueError, match="Matrix must be square"):
        reverse_matrix_elements([
            [1, 2, 3],
            [4, 5]
        ])

def test_matrix_size_too_large_raises_error():
    """Test that matrix larger than 1000x1000 raises ValueError"""
    large_matrix = [[0 for _ in range(1001)] for _ in range(1001)]
    with pytest.raises(ValueError, match="Matrix size must be between 1 and 1000"):
        reverse_matrix_elements(large_matrix)

def test_matrix_with_invalid_elements_raises_error():
    """Test that matrix with elements outside [0, 9] raises ValueError"""
    invalid_matrix = [
        [1, 2, 10],
        [3, 4, 5],
        [6, 7, 8]
    ]
    with pytest.raises(ValueError, match="Matrix elements must be in range"):
        reverse_matrix_elements(invalid_matrix)