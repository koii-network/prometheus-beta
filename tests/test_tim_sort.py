import pytest
from src.tim_sort import tim_sort

def test_tim_sort_empty_list():
    """Test sorting an empty list."""
    assert tim_sort([]) == []

def test_tim_sort_single_element():
    """Test sorting a list with a single element."""
    assert tim_sort([5]) == [5]

def test_tim_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert tim_sort(input_list) == input_list

def test_tim_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    assert tim_sort(input_list) == [1, 2, 3, 4, 5]

def test_tim_sort_random_list():
    """Test sorting a list with random elements."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert tim_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_tim_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    input_list = [5, 2, 9, 1, 5, 6, 2]
    assert tim_sort(input_list) == [1, 2, 2, 5, 5, 6, 9]

def test_tim_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 2, -10, 0, 7, -3]
    assert tim_sort(input_list) == [-10, -5, -3, 0, 2, 7]

def test_tim_sort_raises_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        tim_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        tim_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        tim_sort(None)

def test_tim_sort_original_list_unchanged():
    """Ensure the original list is not modified."""
    input_list = [5, 2, 9, 1]
    result = tim_sort(input_list)
    assert result == [1, 2, 5, 9]
    assert input_list == [5, 2, 9, 1]  # Original list should remain unchanged