import pytest
from src.insertion_sort import insertion_sort

def test_basic_sorting():
    """Test sorting a list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert insertion_sort(input_list) == expected

def test_already_sorted_list():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert insertion_sort(input_list) == expected

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert insertion_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list."""
    assert insertion_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert insertion_sort(input_list) == input_list

def test_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-1, -3, 5, 0, -2, 4]
    expected = [-3, -2, -1, 0, 4, 5]
    assert insertion_sort(input_list) == expected

def test_float_numbers():
    """Test sorting a list with float numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert insertion_sort(input_list) == expected

def test_input_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        insertion_sort(123)

def test_unorderable_list():
    """Test handling of lists with incomparable elements."""
    with pytest.raises(TypeError):
        mixed_list = [1, "a", None]
        insertion_sort(mixed_list)

def test_original_list_unchanged():
    """Verify that the original list is not modified."""
    input_list = [3, 1, 4, 1, 5]
    original_copy = input_list.copy()
    insertion_sort(input_list)
    assert input_list == original_copy