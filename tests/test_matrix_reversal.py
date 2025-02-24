import pytest
from src.matrix_reversal import reverse_matrix_elements

def test_reverse_matrix_elements_basic():
    # Test basic reversal
    matrix = [[1, 23], [45, 6]]
    expected = [[1, 32], [54, 6]]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_single_digit():
    # Test single-digit numbers
    matrix = [[1, 2], [3, 4]]
    expected = [[1, 2], [3, 4]]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_zeros():
    # Test matrix with zeros
    matrix = [[0, 10], [5, 0]]
    expected = [[0, 1], [5, 0]]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_large_matrix():
    # Test a larger matrix
    matrix = [[12, 34, 56], [78, 90, 12], [34, 56, 78]]
    expected = [[21, 43, 65], [87, 09, 21], [43, 65, 87]]
    assert reverse_matrix_elements(matrix) == expected

def test_reverse_matrix_elements_invalid_size():
    # Test non-square matrix
    with pytest.raises(ValueError, match="Matrix must be square"):
        reverse_matrix_elements([[1, 2], [3, 4, 5]])

def test_reverse_matrix_elements_out_of_range():
    # Test matrix with elements outside [0, 9]
    with pytest.raises(ValueError, match="Matrix elements must be integers between 0 and 9"):
        reverse_matrix_elements([[1, 10], [3, 4]])

def test_reverse_matrix_elements_empty_matrix():
    # Test empty matrix
    with pytest.raises(ValueError, match="Matrix size must be between 1 and 1000"):
        reverse_matrix_elements([])

def test_reverse_matrix_elements_too_large_matrix():
    # Test matrix larger than 1000x1000
    large_matrix = [[i for i in range(1001)] for _ in range(1001)]
    with pytest.raises(ValueError, match="Matrix size must be between 1 and 1000"):
        reverse_matrix_elements(large_matrix)