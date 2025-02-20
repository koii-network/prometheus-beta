import pytest
from src.unique_sorted_integers import get_unique_sorted_integers

def test_unique_sorted_integers_basic():
    """Test basic functionality with a list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = get_unique_sorted_integers(input_list)
    assert result == [1, 2, 3, 4, 5, 6, 9]

def test_unique_sorted_integers_already_sorted():
    """Test with an already sorted list with duplicates"""
    input_list = [1, 2, 2, 3, 4, 4, 5]
    result = get_unique_sorted_integers(input_list)
    assert result == [1, 2, 3, 4, 5]

def test_unique_sorted_integers_empty_list():
    """Test with an empty list"""
    input_list = []
    result = get_unique_sorted_integers(input_list)
    assert result == []

def test_unique_sorted_integers_negative_numbers():
    """Test with negative numbers and unsorted input"""
    input_list = [-3, 0, -1, 2, -2, 1, 0]
    result = get_unique_sorted_integers(input_list)
    assert result == [-3, -2, -1, 0, 1, 2]

def test_unique_sorted_integers_invalid_input_type():
    """Test that function raises TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_unique_sorted_integers_invalid_element_type():
    """Test that function raises TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])