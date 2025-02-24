import pytest
from src.second_highest import find_second_highest

def test_sorted_ascending():
    """Test finding second highest in an ascending sorted list"""
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_sorted_descending():
    """Test finding second highest in a descending sorted list"""
    assert find_second_highest([5, 4, 3, 2, 1]) == 4

def test_with_duplicates():
    """Test handling of duplicate values"""
    assert find_second_highest([1, 2, 2, 3, 3, 4, 5]) == 4

def test_all_same_values():
    """Test list with all identical values"""
    assert find_second_highest([2, 2, 2, 2]) is None

def test_two_element_list():
    """Test list with exactly two elements"""
    assert find_second_highest([1, 2]) == 1

def test_empty_list():
    """Test empty list"""
    assert find_second_highest([]) is None

def test_single_element_list():
    """Test list with single element"""
    assert find_second_highest([42]) is None

def test_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        find_second_highest("not a list")

def test_non_integer_elements():
    """Test list with non-integer elements"""
    with pytest.raises(ValueError):
        find_second_highest([1, 2, "three", 4])

def test_negative_numbers():
    """Test list with negative numbers"""
    assert find_second_highest([-5, -4, -3, -2, -1]) == -2

def test_mixed_positive_negative_numbers():
    """Test list with mixed positive and negative numbers"""
    assert find_second_highest([-3, -2, 0, 1, 2, 3]) == 2