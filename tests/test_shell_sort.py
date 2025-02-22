import pytest
from src.shell_sort import shell_sort

def test_shell_sort_basic_list():
    """Test shell sort with a basic unsorted list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = shell_sort(arr)
    assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]

def test_shell_sort_empty_list():
    """Test shell sort with an empty list"""
    arr = []
    sorted_arr = shell_sort(arr)
    assert sorted_arr == []

def test_shell_sort_already_sorted():
    """Test shell sort with an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = shell_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5]

def test_shell_sort_reverse_sorted():
    """Test shell sort with a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = shell_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5]

def test_shell_sort_with_duplicates():
    """Test shell sort with a list containing duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    sorted_arr = shell_sort(arr)
    assert sorted_arr == [1, 2, 2, 3, 3, 4, 8]

def test_shell_sort_floats():
    """Test shell sort with floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    sorted_arr = shell_sort(arr)
    assert sorted_arr == [0.58, 1.41, 2.71, 3.14]

def test_shell_sort_invalid_input():
    """Test shell sort with an invalid input type"""
    with pytest.raises(TypeError):
        shell_sort("not a list")

def test_shell_sort_with_strings():
    """Test shell sort with a list of strings"""
    arr = ["banana", "apple", "cherry", "date"]
    sorted_arr = shell_sort(arr)
    assert sorted_arr == ["apple", "banana", "cherry", "date"]