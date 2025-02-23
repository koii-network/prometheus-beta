import pytest
from src.insertion_sort import insertion_sort

def test_insertion_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert insertion_sort(input_list) == expected

def test_insertion_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    expected = input_list.copy()
    assert insertion_sort(input_list) == expected

def test_insertion_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert insertion_sort(input_list) == expected

def test_insertion_sort_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert insertion_sort(input_list) == expected

def test_insertion_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    expected = []
    assert insertion_sort(input_list) == expected

def test_insertion_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    expected = [42]
    assert insertion_sort(input_list) == expected

def test_insertion_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 0, -3, 10, -1, 7]
    expected = sorted(input_list)
    assert insertion_sort(input_list) == expected

def test_insertion_sort_floating_point():
    """Test sorting a list with floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert insertion_sort(input_list) == expected

def test_insertion_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")

def test_insertion_sort_uncomparable_elements():
    """Test handling of uncomparable elements."""
    # This test ensures the function handles type comparison correctly
    with pytest.raises(TypeError):
        insertion_sort([1, "a", 3])  # Mixed incomparable types