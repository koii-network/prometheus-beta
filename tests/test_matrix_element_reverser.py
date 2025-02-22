import pytest
from src.matrix_element_reverser import reverse_matrix_elements

def test_basic_matrix_reversal():
    input_matrix = [
        [1, 23, 456],
        [7, 89, 0],
        [5, 6, 7]
    ]
    expected_matrix = [
        [1, 32, 654],
        [7, 98, 0],
        [5, 6, 7]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix

def test_single_element_matrix():
    input_matrix = [[5]]
    assert reverse_matrix_elements(input_matrix) == [[5]]

def test_single_digit_matrix():
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert reverse_matrix_elements(input_matrix) == input_matrix

def test_zero_matrix():
    input_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert reverse_matrix_elements(input_matrix) == input_matrix

def test_invalid_input_not_square():
    with pytest.raises(ValueError, match="Matrix must be square"):
        reverse_matrix_elements([
            [1, 2, 3],
            [4, 5]
        ])

def test_invalid_input_out_of_range():
    with pytest.raises(ValueError, match="Matrix must contain integers between 0 and 9"):
        reverse_matrix_elements([
            [1, 2, 10],
            [4, 5, 6],
            [7, 8, 9]
        ])

def test_invalid_input_type():
    with pytest.raises(ValueError, match="Input must be a non-empty list"):
        reverse_matrix_elements([])

def test_large_element_reversal():
    input_matrix = [
        [123, 456],
        [789, 0]
    ]
    expected_matrix = [
        [321, 654],
        [987, 0]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix