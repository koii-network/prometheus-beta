import pytest
from src.k_largest import k_largest

def test_k_largest_normal_case():
    """Test k_largest with a normal input array"""
    assert k_largest([3, 1, 4, 1, 5, 9, 2, 6], 3) == [9, 6, 5]

def test_k_largest_duplicate_elements():
    """Test k_largest with duplicate elements"""
    assert k_largest([1, 1, 1, 2, 2, 3], 3) == [3, 2, 2]

def test_k_largest_small_array():
    """Test k_largest with a small array"""
    assert k_largest([5, 2], 2) == [5, 2]

def test_k_largest_k_one():
    """Test k_largest when k is 1"""
    assert k_largest([3, 1, 4, 1, 5, 9, 2, 6], 1) == [9]

def test_k_largest_negative_k():
    """Test k_largest with negative k"""
    with pytest.raises(ValueError, match="k cannot be negative"):
        k_largest([1, 2, 3], -1)

def test_k_largest_k_too_large():
    """Test k_largest when k is larger than array length"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        k_largest([1, 2, 3], 4)

def test_k_largest_invalid_arr_type():
    """Test k_largest with invalid array type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        k_largest("not a list", 2)

def test_k_largest_invalid_k_type():
    """Test k_largest with invalid k type"""
    with pytest.raises(TypeError, match="k must be an integer"):
        k_largest([1, 2, 3], "not an int")