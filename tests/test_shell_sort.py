import pytest
from src.shell_sort import shell_sort

def test_shell_sort_basic_list():
    """Test sorting a basic list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    result = shell_sort(arr)
    assert result == [11, 12, 22, 25, 34, 64, 90]
    assert result is arr  # Ensure in-place sorting

def test_shell_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    result = shell_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_shell_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    result = shell_sort(arr)
    assert result == [1, 2, 3, 4, 5]

def test_shell_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    result = shell_sort(arr)
    assert result == []

def test_shell_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    result = shell_sort(arr)
    assert result == [42]

def test_shell_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    result = shell_sort(arr)
    assert result == [1, 2, 2, 3, 3, 4, 8]

def test_shell_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    result = shell_sort(arr)
    assert result == [0.58, 1.41, 2.71, 3.14]

def test_shell_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        shell_sort("not a list")

def test_shell_sort_large_list():
    """Test sorting a larger list to stress the algorithm."""
    import random
    random.seed(42)  # For reproducibility
    arr = [random.randint(1, 1000) for _ in range(100)]
    sorted_arr = sorted(arr)
    result = shell_sort(arr)
    assert result == sorted_arr