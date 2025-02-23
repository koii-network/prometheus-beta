import pytest
from src.unique_sorted_list import get_unique_sorted_list

def test_basic_functionality():
    """Test basic list of integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert get_unique_sorted_list(input_list) == [1, 2, 3, 4, 5, 6, 9]

def test_already_sorted():
    """Test list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert get_unique_sorted_list(input_list) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test empty list."""
    assert get_unique_sorted_list([]) == []

def test_single_element():
    """Test list with a single element."""
    assert get_unique_sorted_list([42]) == [42]

def test_all_duplicates():
    """Test list with all duplicate elements."""
    assert get_unique_sorted_list([7, 7, 7, 7]) == [7]

def test_negative_numbers():
    """Test list with negative numbers."""
    input_list = [-3, -1, -4, -1, -5, 0, 5]
    assert get_unique_sorted_list(input_list) == [-5, -4, -3, -1, 0, 5]

def test_non_list_input():
    """Test non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_list(42)

def test_non_integer_input():
    """Test list with non-integer elements raises TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_list([1, 2, "3", 4])

def test_mixed_positive_negative():
    """Test list with mixed positive and negative integers."""
    input_list = [3, -1, 0, 3, -1, 5, -5, 0]
    assert get_unique_sorted_list(input_list) == [-5, -1, 0, 3, 5]