import pytest
from src.shell_sort import shell_sort

def test_shell_sort_empty_list():
    """Test shell sort with an empty list."""
    assert shell_sort([]) == []

def test_shell_sort_single_element():
    """Test shell sort with a single element list."""
    assert shell_sort([5]) == [5]

def test_shell_sort_already_sorted():
    """Test shell sort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_reverse_sorted():
    """Test shell sort with a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_random_list():
    """Test shell sort with a random list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert shell_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_shell_sort_with_duplicates():
    """Test shell sort with a list containing duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert shell_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_shell_sort_invalid_input():
    """Test shell sort with an invalid input type."""
    with pytest.raises(TypeError):
        shell_sort("not a list")
    with pytest.raises(TypeError):
        shell_sort(123)
    with pytest.raises(TypeError):
        shell_sort(None)