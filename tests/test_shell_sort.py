import pytest
from src.shell_sort import shell_sort

def test_shell_sort_normal_list():
    """Test shell sort with a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_already_sorted():
    """Test shell sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert shell_sort(input_list) == input_list

def test_shell_sort_reverse_sorted():
    """Test shell sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_empty_list():
    """Test shell sort with an empty list."""
    assert shell_sort([]) == []

def test_shell_sort_single_element():
    """Test shell sort with a single-element list."""
    input_list = [42]
    assert shell_sort(input_list) == input_list

def test_shell_sort_duplicate_elements():
    """Test shell sort with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_negative_numbers():
    """Test shell sort with negative numbers."""
    input_list = [-5, 3, -2, 0, 1, -7, 4]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_float_numbers():
    """Test shell sort with floating point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_invalid_input():
    """Test shell sort with invalid input type."""
    with pytest.raises(TypeError):
        shell_sort("not a list")
    
    with pytest.raises(TypeError):
        shell_sort(123)