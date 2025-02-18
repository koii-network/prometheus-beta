import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_empty_list():
    """Test sorting an empty list"""
    assert bitonic_sort([]) == []

def test_bitonic_sort_single_element():
    """Test sorting a list with a single element"""
    assert bitonic_sort([5]) == [5]

def test_bitonic_sort_ascending_integers():
    """Test sorting integers in ascending order"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bitonic_sort(arr) == sorted(arr)

def test_bitonic_sort_descending_integers():
    """Test sorting integers in descending order"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert bitonic_sort(arr, ascending=False) == sorted(arr, reverse=True)

def test_bitonic_sort_floating_point():
    """Test sorting floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert bitonic_sort(arr) == sorted(arr)

def test_bitonic_sort_negative_numbers():
    """Test sorting list with negative numbers"""
    arr = [-5, 20, -3, 0, 12, -15, 7]
    assert bitonic_sort(arr) == sorted(arr)

def test_bitonic_sort_input_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_bitonic_sort_mixed_type_error():
    """Test that ValueError is raised for mixed type elements"""
    with pytest.raises(ValueError):
        bitonic_sort([1, 2, "3", 4.0])

def test_bitonic_sort_original_list_unchanged():
    """Test that the original list is not modified"""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    bitonic_sort(arr)
    assert arr == original