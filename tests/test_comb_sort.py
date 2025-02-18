import pytest
from src.comb_sort import comb_sort

def test_comb_sort_normal_list():
    """Test sorting a normal list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = comb_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_comb_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = comb_sort(arr.copy())
    assert sorted_arr == arr

def test_comb_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = comb_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_comb_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    sorted_arr = comb_sort(arr.copy())
    assert sorted_arr == []

def test_comb_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    sorted_arr = comb_sort(arr.copy())
    assert sorted_arr == arr

def test_comb_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = comb_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_comb_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        comb_sort("not a list")
    with pytest.raises(TypeError):
        comb_sort(123)
    with pytest.raises(TypeError):
        comb_sort(None)