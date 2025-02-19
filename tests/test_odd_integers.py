import pytest
from src.odd_integers import filter_odd_integers

def test_filter_odd_integers_basic():
    """Test filtering and sorting odd integers from a mixed list"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert filter_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_filter_odd_integers_empty_list():
    """Test with an empty list"""
    assert filter_odd_integers([]) == []

def test_filter_odd_integers_only_even():
    """Test list with only even numbers"""
    assert filter_odd_integers([2, 4, 6, 8]) == []

def test_filter_odd_integers_only_odd():
    """Test list with only odd numbers"""
    assert filter_odd_integers([1, 3, 5, 7]) == [1, 3, 5, 7]

def test_filter_odd_integers_negative_numbers():
    """Test with negative and positive odd and even numbers"""
    input_list = [-3, -2, -1, 0, 1, 2, 3]
    assert filter_odd_integers(input_list) == [-3, -1, 1, 3]

def test_filter_odd_integers_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_integers("not a list")

def test_filter_odd_integers_invalid_element_type():
    """Test raising TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_odd_integers([1, 2, "3", 4])