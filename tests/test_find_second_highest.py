import pytest
from src.find_second_highest import find_second_highest

def test_find_second_highest_normal_case():
    """Test finding second highest in a standard sorted list"""
    assert find_second_highest([1, 2, 3, 4, 5]) == 4

def test_find_second_highest_with_duplicates():
    """Test finding second highest with duplicate values"""
    assert find_second_highest([1, 2, 2, 3, 3, 5, 5]) == 3

def test_find_second_highest_all_same_values():
    """Test list with all same values returns None"""
    assert find_second_highest([1, 1, 1, 1]) is None

def test_find_second_highest_two_unique_values():
    """Test list with only two unique values"""
    assert find_second_highest([1, 2]) == 1

def test_find_second_highest_raises_on_empty_list():
    """Test that empty list raises ValueError"""
    with pytest.raises(ValueError):
        find_second_highest([])

def test_find_second_highest_raises_on_non_list():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        find_second_highest("not a list")

def test_find_second_highest_single_element():
    """Test list with single element returns None"""
    assert find_second_highest([1]) is None