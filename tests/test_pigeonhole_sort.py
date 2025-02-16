import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_pigeonhole_sort_normal_case():
    """Test sorting a list of integers."""
    input_list = [8, 3, 2, 7, 4, 6, 8]
    expected = [2, 3, 4, 6, 7, 8, 8]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == input_list

def test_pigeonhole_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_with_duplicates():
    """Test sorting a list with multiple duplicate values."""
    input_list = [4, 2, 4, 1, 2, 4, 1]
    expected = [1, 1, 2, 2, 4, 4, 4]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_empty_list():
    """Test sorting an empty list."""
    assert pigeonhole_sort([]) == []

def test_pigeonhole_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert pigeonhole_sort(input_list) == input_list

def test_pigeonhole_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, -2, -8, -1, -3]
    expected = [-8, -5, -3, -2, -1]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_mixed_positive_negative():
    """Test sorting a list with mixed positive and negative numbers."""
    input_list = [3, -1, 0, 4, -5, 2]
    expected = [-5, -1, 0, 2, 3, 4]
    assert pigeonhole_sort(input_list) == expected

def test_pigeonhole_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort("not a list")

def test_pigeonhole_sort_invalid_element_type():
    """Test that a ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        pigeonhole_sort([1, 2, "3", 4])