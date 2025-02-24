import pytest
from src.k_largest import k_largest

def test_k_largest_normal_case():
    """Test k_largest with a normal input scenario"""
    assert k_largest([3, 1, 5, 12, 2, 11], 3) == [12, 11, 5]

def test_k_largest_unsorted_input():
    """Test k_largest with an unsorted input"""
    assert k_largest([5, 2, 9, 1, 7, 6], 2) == [9, 7]

def test_k_largest_with_duplicates():
    """Test k_largest with duplicate values"""
    assert k_largest([3, 3, 3, 2, 1, 4], 3) == [4, 3, 3]

def test_k_largest_zero_k():
    """Test k_largest when k is zero"""
    assert k_largest([1, 2, 3], 0) == []

def test_k_largest_entire_array():
    """Test k_largest when k equals array length"""
    assert k_largest([1, 2, 3, 4], 4) == [4, 3, 2, 1]

def test_k_largest_negative_k():
    """Test k_largest raises ValueError for negative k"""
    with pytest.raises(ValueError, match="k cannot be negative"):
        k_largest([1, 2, 3], -1)

def test_k_largest_k_too_large():
    """Test k_largest raises ValueError when k is larger than array length"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        k_largest([1, 2, 3], 4)

def test_k_largest_non_list_input():
    """Test k_largest raises TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        k_largest("not a list", 2)

def test_k_largest_non_integer_elements():
    """Test k_largest raises TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        k_largest([1, 2, "3"], 2)

def test_k_largest_empty_array():
    """Test k_largest with an empty array"""
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        k_largest([], 1)