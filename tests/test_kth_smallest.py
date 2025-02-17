import pytest
from src.kth_smallest import find_kth_smallest

def test_find_kth_smallest_normal_case():
    """Test finding kth smallest in a normal list"""
    arr = [7, 10, 4, 3, 20, 15]
    assert find_kth_smallest(arr, 3) == 7

def test_find_kth_smallest_sorted_list():
    """Test finding kth smallest in an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert find_kth_smallest(arr, 4) == 4

def test_find_kth_smallest_reverse_sorted():
    """Test finding kth smallest in a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert find_kth_smallest(arr, 2) == 2

def test_find_kth_smallest_first_element():
    """Test finding the first smallest element"""
    arr = [10, 5, 8, 2, 7]
    assert find_kth_smallest(arr, 1) == 2

def test_find_kth_smallest_last_element():
    """Test finding the last smallest element"""
    arr = [10, 5, 8, 2, 7]
    assert find_kth_smallest(arr, 5) == 10

def test_kth_smallest_invalid_k_too_low():
    """Test that ValueError is raised when k is less than 1"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 0)

def test_kth_smallest_invalid_k_too_high():
    """Test that ValueError is raised when k is greater than array length"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be between 1 and 3"):
        find_kth_smallest(arr, 4)

def test_kth_smallest_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_kth_smallest("not a list", 2)

def test_kth_smallest_invalid_k_type():
    """Test that TypeError is raised for non-integer k"""
    arr = [1, 2, 3]
    with pytest.raises(TypeError, match="k must be an integer"):
        find_kth_smallest(arr, "2")

def test_kth_smallest_empty_list():
    """Test that ValueError is raised for an empty list"""
    with pytest.raises(ValueError, match="k must be between 1 and 0"):
        find_kth_smallest([], 1)