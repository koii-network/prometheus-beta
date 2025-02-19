import pytest
from src.array_subtraction import subtract_arrays_mod_10

def test_subtract_arrays_mod_10_normal_case():
    """Test normal subtraction with different scenarios"""
    A = [7, 5, 3, 9, 2, 6, 8, 1, 4, 0]
    B = [2, 3, 1, 4, 5, 1, 3, 7, 2, 9]
    expected = [5, 2, 2, 5, 7, 5, 5, 4, 2, 1]
    assert subtract_arrays_mod_10(A, B) == expected

def test_subtract_arrays_mod_10_negative_results():
    """Test cases where subtraction results would be negative"""
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 9, 0]
    assert subtract_arrays_mod_10(A, B) == expected

def test_subtract_arrays_mod_10_equal_arrays():
    """Test subtraction of identical arrays"""
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert subtract_arrays_mod_10(A, B) == expected

def test_subtract_arrays_mod_10_invalid_length():
    """Test that function raises error for arrays not of length 10"""
    A = [1, 2, 3]
    B = [4, 5, 6]
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        subtract_arrays_mod_10(A, B)

def test_subtract_arrays_mod_10_large_numbers():
    """Test subtraction with large numbers"""
    A = [99, 88, 77, 66, 55, 44, 33, 22, 11, 100]
    B = [50, 40, 30, 20, 10, 5, 15, 25, 35, 45]
    expected = [4, 4, 4, 4, 4, 9, 8, 7, 6, 5]
    assert subtract_arrays_mod_10(A, B) == expected