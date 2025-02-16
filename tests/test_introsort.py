import pytest
from src.introsort import introsort

def test_introsort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert introsort(arr) == []

def test_introsort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert introsort(arr) == [42]

def test_introsort_sorted_list():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert introsort(arr) == [1, 2, 3, 4, 5]

def test_introsort_random_list():
    """Test sorting a random list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert introsort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_introsort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert introsort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_introsort_large_list():
    """Test sorting a large list."""
    import random
    arr = [random.randint(1, 1000) for _ in range(1000)]
    assert introsort(arr) == sorted(arr)

def test_introsort_original_list_unchanged():
    """Test that the original list remains unchanged."""
    arr = [5, 2, 9, 1, 7]
    original = arr.copy()
    introsort(arr)
    assert arr == original

def test_introsort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, 2, -10, 0, 7, -3]
    assert introsort(arr) == [-10, -5, -3, 0, 2, 7]

def test_introsort_mixed_types_error():
    """Test that introsort raises TypeError for mixed types."""
    arr = [1, 2, 'a', 4, 'b']
    with pytest.raises(TypeError):
        introsort(arr)