import pytest
from src.matrix_reversal import reverse_matrix_elements

def test_basic_matrix_reversal():
    # Basic test with single-digit numbers
    matrix = [[1, 2], [3, 4]]
    expected = [[1, 2], [3, 4]]
    assert reverse_matrix_elements(matrix) == expected

def test_multi_digit_reversal():
    # Ensure multi-digit numbers are not allowed
    with pytest.raises(ValueError):
        reverse_matrix_elements([[10, 2], [3, 4]])

def test_reverse_single_digit_numbers():
    matrix = [[5, 6], [7, 8]]
    expected = [[5, 6], [7, 8]]
    assert reverse_matrix_elements(matrix) == expected

def test_matrix_reversal_single_element():
    matrix = [[7]]
    expected = [[7]]
    assert reverse_matrix_elements(matrix) == expected

def test_invalid_matrix_not_square():
    with pytest.raises(ValueError):
        reverse_matrix_elements([[1, 2], [3]])

def test_matrix_outside_size_range():
    # Test empty matrix
    with pytest.raises(ValueError):
        reverse_matrix_elements([])
    
    # Test matrix with over 1000 elements (create large matrix)
    large_matrix = [[i % 10 for _ in range(1001)] for i in range(1001)]
    with pytest.raises(ValueError):
        reverse_matrix_elements(large_matrix)

def test_matrix_element_validation():
    # Test matrix with elements outside [0, 9]
    with pytest.raises(ValueError):
        reverse_matrix_elements([[10, 2], [3, 4]])
    
    with pytest.raises(ValueError):
        reverse_matrix_elements([[-1, 2], [3, 4]])

def test_zero_elements():
    matrix = [[0, 0], [0, 0]]
    expected = [[0, 0], [0, 0]]
    assert reverse_matrix_elements(matrix) == expected