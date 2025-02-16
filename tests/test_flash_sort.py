import pytest
import random
from src.flash_sort import flash_sort

def test_flash_sort_empty_list():
    """Test sorting an empty list."""
    assert flash_sort([]) == []

def test_flash_sort_single_element():
    """Test sorting a list with a single element."""
    assert flash_sort([42]) == [42]

def test_flash_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert flash_sort(arr) == [1, 2, 3, 4, 5]

def test_flash_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert flash_sort(arr) == [1, 2, 3, 4, 5]

def test_flash_sort_random_list():
    """Test sorting a random list of integers."""
    arr = [5, 2, 9, 1, 7, 6, 3]
    assert flash_sort(arr) == [1, 2, 3, 5, 6, 7, 9]

def test_flash_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert flash_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_flash_sort_with_large_random_list():
    """Test sorting a large random list."""
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    assert flash_sort(arr) == sorted(arr)

def test_flash_sort_with_floating_point():
    """Test sorting a list of floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert flash_sort(arr) == [0.58, 1.41, 2.23, 2.71, 3.14]

def test_flash_sort_raises_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        flash_sort("not a list")

def test_flash_sort_input_not_modified():
    """Ensure the original input list is not modified."""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    flash_sort(arr)
    assert arr == original

def test_flash_sort_with_non_comparable_elements():
    """Test that ValueError is raised for non-comparable elements."""
    with pytest.raises(ValueError):
        flash_sort([1, 2, 'a', 3])