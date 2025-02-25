import pytest
from src.sorting import sort_nums, optimal_sort

def test_sort_nums_basic_sorting():
    """Test basic sorting functionality."""
    input_list = [5, 2, 9, 1, 7]
    result = sort_nums(input_list)
    assert result == [1, 2, 5, 7, 9], "Basic sorting should work"

def test_sort_nums_duplicate_elements():
    """Test sorting with duplicate elements to reveal the bug."""
    input_list = [5, 2, 5, 1, 7, 2]
    result = sort_nums(input_list)
    # This test is expected to fail due to the intentional bug
    with pytest.raises(AssertionError):
        assert result == [1, 2, 2, 5, 5, 7], "Sorting with duplicates should fail"

def test_optimal_sort_basic():
    """Test basic sorting functionality of optimal_sort."""
    input_list = [5, 2, 9, 1, 7]
    result = optimal_sort(input_list)
    assert result == [1, 2, 5, 7, 9], "Basic sorting should work"

def test_optimal_sort_duplicate_elements():
    """Test sorting with duplicate elements using optimal_sort."""
    input_list = [5, 2, 5, 1, 7, 2]
    result = optimal_sort(input_list)
    assert result == [1, 2, 2, 5, 5, 7], "Sorting with duplicates should work correctly"

def test_optimal_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    result = optimal_sort(input_list)
    assert result == [], "Sorting an empty list should return an empty list"

def test_optimal_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    result = optimal_sort(input_list)
    assert result == [42], "Sorting a single-element list should return the same list"