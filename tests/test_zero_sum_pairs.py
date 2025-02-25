import pytest
from src.zero_sum_pairs import count_zero_sum_pairs

def test_basic_zero_sum_pairs():
    """Test basic scenario with zero-sum pairs"""
    assert count_zero_sum_pairs([1, -1, 2, -2, 3]) == 2

def test_empty_list():
    """Test empty list returns zero pairs"""
    assert count_zero_sum_pairs([]) == 0

def test_no_zero_sum_pairs():
    """Test list with no zero-sum pairs"""
    assert count_zero_sum_pairs([1, 2, 3, 4]) == 0

def test_multiple_same_pair():
    """Test list with multiple instances of the same zero-sum pair"""
    assert count_zero_sum_pairs([1, -1, 1, -1]) == 4

def test_zero_pairs():
    """Test list with zero pairs"""
    assert count_zero_sum_pairs([0, 0, 0]) == 3

def test_invalid_input_non_list():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        count_zero_sum_pairs("not a list")

def test_invalid_input_non_integers():
    """Test that list with non-integer elements raises ValueError"""
    with pytest.raises(ValueError):
        count_zero_sum_pairs([1, 2, "3"])

def test_large_input():
    """Test larger input with multiple zero-sum pairs"""
    input_list = [1, -1, 2, -2, 3, -3, 4, -4, 0, 0]
    assert count_zero_sum_pairs(input_list) == 8