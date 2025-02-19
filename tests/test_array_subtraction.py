import pytest
from src.array_subtraction import subtract_arrays_mod_10

def test_subtract_arrays_mod_10_basic():
    A = [5, 7, 3, 9, 2, 1, 8, 6, 4, 0]
    B = [2, 3, 1, 4, 5, 6, 3, 2, 9, 7]
    expected = [3, 4, 2, 5, 7, 5, 5, 4, 5, 3]
    assert subtract_arrays_mod_10(A, B) == expected

def test_subtract_arrays_mod_10_negative_results():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
    expected = [0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
    assert subtract_arrays_mod_10(A, B) == expected

def test_subtract_arrays_mod_10_zero_result():
    A = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    B = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert subtract_arrays_mod_10(A, B) == expected

def test_subtract_arrays_mod_10_invalid_length():
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        subtract_arrays_mod_10([1, 2, 3], [4, 5, 6])

def test_subtract_arrays_mod_10_edge_cases():
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    B = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    expected = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
    assert subtract_arrays_mod_10(A, B) == expected