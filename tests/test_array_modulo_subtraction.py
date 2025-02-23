import pytest
from src.array_modulo_subtraction import modulo_subtraction

def test_basic_modulo_subtraction():
    """Test basic modulo subtraction with positive integers"""
    A = [7, 5, 3, 8, 2, 9, 1, 6, 4, 0]
    B = [3, 2, 1, 4, 5, 6, 7, 8, 9, 2]
    expected = [4, 3, 2, 4, 7, 3, 4, 8, 5, 8]
    assert modulo_subtraction(A, B) == expected

def test_negative_results():
    """Test cases where subtraction results in negative numbers"""
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 9, 0]
    assert modulo_subtraction(A, B) == expected

def test_zero_array():
    """Test with one array of zeros"""
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    B = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert modulo_subtraction(A, B) == expected

def test_invalid_input_length():
    """Test that function raises ValueError for incorrect array lengths"""
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        modulo_subtraction([1, 2, 3], [4, 5, 6])
    
    with pytest.raises(ValueError, match="Both input arrays must be of length 10"):
        modulo_subtraction([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], [1, 2, 3])