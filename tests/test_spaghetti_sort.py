import pytest
import random
from src.spaghetti_sort import spaghetti_sort, is_sorted

def test_spaghetti_sort_empty_list():
    """Test sorting an empty list"""
    assert spaghetti_sort([]) == []

def test_spaghetti_sort_single_element():
    """Test sorting a list with a single element"""
    assert spaghetti_sort([5]) == [5]

def test_spaghetti_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert spaghetti_sort(arr) == [1, 2, 3, 4, 5]

def test_spaghetti_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    result = spaghetti_sort(arr)
    assert is_sorted(result)
    assert set(result) == set(arr)

def test_spaghetti_sort_random_list():
    """Test sorting a random list"""
    random.seed(42)  # for reproducibility
    arr = [random.randint(1, 100) for _ in range(10)]
    result = spaghetti_sort(arr)
    assert is_sorted(result)
    assert set(result) == set(arr)

def test_spaghetti_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = spaghetti_sort(arr)
    assert is_sorted(result)
    assert set(result) == set(arr)

def test_spaghetti_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        spaghetti_sort("not a list")
    with pytest.raises(TypeError):
        spaghetti_sort(123)
    with pytest.raises(TypeError):
        spaghetti_sort(None)

def test_is_sorted_function():
    """Test the is_sorted helper function"""
    from src.spaghetti_sort import is_sorted
    
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([5, 5, 5, 5]) == True
    assert is_sorted([1]) == True
    assert is_sorted([]) == True
    assert is_sorted([5, 3, 1]) == False
    assert is_sorted([1, 3, 2, 4]) == False