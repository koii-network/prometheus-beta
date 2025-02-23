import pytest
from src.gravity_sort import gravity_sort

def test_gravity_sort_normal_case():
    """Test gravity sort with a standard list of positive integers."""
    input_list = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_already_sorted():
    """Test gravity sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert gravity_sort(input_list) == input_list

def test_gravity_sort_reverse_sorted():
    """Test gravity sort with a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_duplicate_numbers():
    """Test gravity sort with duplicate numbers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = [1, 1, 2, 3, 4, 5, 6, 9]
    assert gravity_sort(input_list) == expected

def test_gravity_sort_empty_list():
    """Test gravity sort with an empty list."""
    assert gravity_sort([]) == []

def test_gravity_sort_single_element():
    """Test gravity sort with a single-element list."""
    assert gravity_sort([42]) == [42]

def test_gravity_sort_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        gravity_sort("not a list")

def test_gravity_sort_non_integer_elements():
    """Test that a list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        gravity_sort([1, 2, "3", 4])

def test_gravity_sort_negative_numbers():
    """Test that a list with negative numbers raises a ValueError."""
    with pytest.raises(ValueError, match="Input cannot contain negative numbers"):
        gravity_sort([1, -2, 3, -4])