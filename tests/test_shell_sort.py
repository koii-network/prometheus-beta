import pytest
from src.shell_sort import shell_sort

def test_shell_sort_standard_list():
    """Test shell sort with a standard unsorted list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert shell_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_shell_sort_already_sorted():
    """Test shell sort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_reverse_sorted():
    """Test shell sort with a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_duplicate_elements():
    """Test shell sort with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert shell_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_shell_sort_empty_list():
    """Test shell sort with an empty list."""
    arr = []
    assert shell_sort(arr) == []

def test_shell_sort_single_element():
    """Test shell sort with a single element."""
    arr = [42]
    assert shell_sort(arr) == [42]

def test_shell_sort_negative_numbers():
    """Test shell sort with negative numbers."""
    arr = [-4, 1, -9, 0, 5, -2]
    assert shell_sort(arr) == [-9, -4, -2, 0, 1, 5]

def test_shell_sort_float_numbers():
    """Test shell sort with floating point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert shell_sort(arr) == [0.58, 1.41, 2.71, 3.14]

def test_shell_sort_invalid_input():
    """Test shell sort with invalid input type."""
    with pytest.raises(TypeError):
        shell_sort("not a list")
    
    with pytest.raises(TypeError):
        shell_sort(None)