import pytest
from src.shell_sort import shell_sort

def test_shell_sort_basic_list():
    """Test sorting a basic list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert shell_sort(input_list) == input_list

def test_shell_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_single_element():
    """Test sorting a single-element list."""
    input_list = [42]
    assert shell_sort(input_list) == input_list

def test_shell_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    assert shell_sort(input_list) == []

def test_shell_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-4, 2, -9, 0, 5, -1]
    expected = sorted(input_list)
    assert shell_sort(input_list) == expected

def test_shell_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shell_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        shell_sort(123)