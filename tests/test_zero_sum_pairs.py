import pytest
from src.zero_sum_pairs import count_zero_sum_pairs

def test_count_zero_sum_pairs_basic():
    """Test basic functionality of counting zero-sum pairs"""
    assert count_zero_sum_pairs([1, -1, 2, -2, 3]) == 2
    assert count_zero_sum_pairs([0, 0, 0]) == 3
    assert count_zero_sum_pairs([1, 2, 3, 4, -1, -2]) == 2

def test_count_zero_sum_pairs_empty():
    """Test with an empty list"""
    assert count_zero_sum_pairs([]) == 0

def test_count_zero_sum_pairs_no_pairs():
    """Test with a list that has no zero-sum pairs"""
    assert count_zero_sum_pairs([1, 2, 3, 4, 5]) == 0

def test_count_zero_sum_pairs_duplicate_pairs():
    """Test with lists containing duplicate numbers"""
    assert count_zero_sum_pairs([1, -1, 1, -1]) == 4

def test_count_zero_sum_pairs_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        count_zero_sum_pairs("not a list")
    with pytest.raises(TypeError):
        count_zero_sum_pairs(123)
    with pytest.raises(TypeError):
        count_zero_sum_pairs(None)