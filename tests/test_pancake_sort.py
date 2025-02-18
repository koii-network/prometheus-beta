import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_empty_list():
    """Test sorting an empty list"""
    assert pancake_sort([]) == []

def test_pancake_sort_single_element():
    """Test sorting a list with a single element"""
    assert pancake_sort([5]) == [5]

def test_pancake_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert pancake_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_pancake_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    assert pancake_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_pancake_sort_random_list():
    """Test sorting a random list of integers"""
    assert pancake_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

def test_pancake_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert pancake_sort([4, 2, 2, 1, 3, 3]) == [1, 2, 2, 3, 3, 4]

def test_pancake_sort_float_numbers():
    """Test sorting a list of float numbers"""
    assert pancake_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_pancake_sort_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        pancake_sort("not a list")

def test_pancake_sort_input_preservation():
    """Ensure the original list is not modified"""
    original = [5, 2, 9, 1, 7]
    pancake_sort(original)
    assert original == [5, 2, 9, 1, 7]