import pytest
from src.count_occurrences import count_occurrences

def test_count_occurrences_normal_case():
    """Test basic functionality of counting occurrences"""
    test_list = [1, 2, 3, 2, 2, 4, 5]
    assert count_occurrences(test_list, 2) == 3

def test_count_occurrences_no_matches():
    """Test when element is not in the list"""
    test_list = [1, 3, 5, 7]
    assert count_occurrences(test_list, 2) == 0

def test_count_occurrences_empty_list():
    """Test with an empty list"""
    test_list = []
    assert count_occurrences(test_list, 1) == 0

def test_count_occurrences_different_types():
    """Test counting with different types of elements"""
    test_list = [1, 'a', 2, 'a', 3, 'a']
    assert count_occurrences(test_list, 'a') == 3

def test_count_occurrences_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences("not a list", 1)
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences(123, 1)
    with pytest.raises(TypeError, match="Input must be a list"):
        count_occurrences(None, 1)