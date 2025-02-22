import pytest
from src.array_diff_modulo import array_diff_modulo

def test_basic_array_diff_modulo():
    A = [5, 7, 3, 8, 9, 2, 1, 6, 4, 0]
    B = [3, 2, 1, 5, 6, 7, 8, 9, 0, 5]
    expected = [2, 5, 2, 3, 3, 5, 3, 7, 4, 5]
    assert array_diff_modulo(A, B) == expected

def test_negative_result_handling():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    expected = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert array_diff_modulo(A, B) == expected

def test_zero_result_handling():
    A = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    B = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert array_diff_modulo(A, B) == expected

def test_input_length_validation():
    with pytest.raises(ValueError, match="Input arrays must be of length 10"):
        array_diff_modulo([1, 2, 3], [4, 5, 6])
    
    with pytest.raises(ValueError, match="Input arrays must be of length 10"):
        array_diff_modulo([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3])

def test_large_numbers_modulo():
    A = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    B = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert array_diff_modulo(A, B) == expected