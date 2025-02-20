import pytest
from src.unique_pairs import get_unique_pairs

def test_get_unique_pairs_basic():
    """Test basic functionality of unique pairs"""
    result = get_unique_pairs([1, 2, 3])
    assert set(result) == {(1, 2), (1, 3), (2, 3)}
    assert len(result) == 3

def test_get_unique_pairs_with_duplicates():
    """Test handling of lists with duplicate elements"""
    result = get_unique_pairs([1, 1, 2, 2, 3])
    assert set(result) == {(1, 2), (1, 3), (2, 3)}
    assert len(result) == 3

def test_get_unique_pairs_empty_list():
    """Test behavior with an empty list"""
    result = get_unique_pairs([])
    assert result == []

def test_get_unique_pairs_single_element():
    """Test behavior with a single-element list"""
    result = get_unique_pairs([5])
    assert result == []

def test_get_unique_pairs_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_pairs("not a list")

def test_get_unique_pairs_non_integer_elements():
    """Test handling of non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        get_unique_pairs([1, 2, "3"])

def test_get_unique_pairs_large_list():
    """Test with a larger list of integers"""
    large_list = list(range(10))
    result = get_unique_pairs(large_list)
    assert len(result) == (len(large_list) * (len(large_list) - 1)) // 2