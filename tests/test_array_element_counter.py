import pytest
from src.array_element_counter import count_element_occurrences

def test_count_element_occurrences_basic():
    """Test basic counting of element occurrences"""
    assert count_element_occurrences([1, 2, 3, 2, 2, 4], 2) == 3
    assert count_element_occurrences(['a', 'b', 'a', 'c'], 'a') == 2

def test_count_element_occurrences_empty_list():
    """Test counting in an empty list"""
    assert count_element_occurrences([], 5) == 0

def test_count_element_occurrences_no_matches():
    """Test when element is not in the list"""
    assert count_element_occurrences([1, 2, 3], 4) == 0

def test_count_element_occurrences_different_types():
    """Test counting with different types of elements"""
    assert count_element_occurrences([1, 'a', 1, 'a', 1], 1) == 3
    assert count_element_occurrences([1, 'a', 1, 'a', 1], 'a') == 2

def test_count_element_occurrences_invalid_input():
    """Test error handling for invalid input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences("not a list", 2)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences(123, 'a')
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences(None, 1)