import pytest
from src.spaghetti_sort import spaghetti_sort

def test_spaghetti_sort_basic():
    """Test basic sorting functionality"""
    assert spaghetti_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_spaghetti_sort_empty_list():
    """Test sorting an empty list"""
    assert spaghetti_sort([]) == []

def test_spaghetti_sort_single_element():
    """Test sorting a list with a single element"""
    assert spaghetti_sort([42]) == [42]

def test_spaghetti_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert spaghetti_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_spaghetti_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert spaghetti_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_spaghetti_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    assert spaghetti_sort([3, 3, 3, 1, 1, 2]) == [1, 1, 2, 3, 3, 3]

def test_spaghetti_sort_zero_and_positive():
    """Test sorting a list with zero and positive numbers"""
    assert spaghetti_sort([0, 5, 0, 3, 2, 0]) == [0, 0, 0, 2, 3, 5]

def test_spaghetti_sort_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        spaghetti_sort("not a list")

def test_spaghetti_sort_negative_numbers():
    """Test raising ValueError for negative numbers"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        spaghetti_sort([-1, 2, 3])

def test_spaghetti_sort_non_integer():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        spaghetti_sort([1, 2.5, 3])