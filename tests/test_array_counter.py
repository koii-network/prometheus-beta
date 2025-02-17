import pytest
from src.array_counter import count_occurrences

def test_count_occurrences_basic():
    """Test basic counting of element occurrences"""
    test_arr = [1, 2, 3, 2, 2, 4, 5]
    assert count_occurrences(test_arr, 2) == 3

def test_count_occurrences_no_matches():
    """Test when element is not in the list"""
    test_arr = [1, 3, 5, 7]
    assert count_occurrences(test_arr, 2) == 0

def test_count_occurrences_empty_list():
    """Test counting in an empty list"""
    test_arr = []
    assert count_occurrences(test_arr, 'any') == 0

def test_count_occurrences_mixed_types():
    """Test counting with mixed type elements"""
    test_arr = [1, '1', 1, '1', 2]
    assert count_occurrences(test_arr, 1) == 2
    assert count_occurrences(test_arr, '1') == 2

def test_count_occurrences_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences("not a list", 1)
        count_occurrences(123, 1)
        count_occurrences(None, 1)