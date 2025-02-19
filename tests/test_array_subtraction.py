import pytest
from src.array_subtraction import subtract_and_modulo_arrays

def test_basic_subtraction():
    A = [5, 7, 3, 9, 2, 6, 8, 1, 4, 0]
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [4, 5, 0, 5, 7, 0, 1, 3, 5, 0]
    assert subtract_and_modulo_arrays(A, B) == expected

def test_negative_result_becomes_zero():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert subtract_and_modulo_arrays(A, B) == expected

def test_same_arrays():
    A = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    B = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert subtract_and_modulo_arrays(A, B) == expected

def test_invalid_array_length():
    A = [1, 2, 3]
    B = [4, 5, 6]
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        subtract_and_modulo_arrays(A, B)