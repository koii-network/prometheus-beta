import pytest
import math
from src.perfect_squares import sum_perfect_squares_from_set

def test_basic_perfect_squares():
    """Test basic scenarios with perfect squares"""
    assert sum_perfect_squares_from_set({4, 9, 16}) == 29  # 4 + 9 + 16
    assert sum_perfect_squares_from_set({1, 4, 9}) == 14   # 1 + 4 + 9

def test_combined_perfect_squares():
    """Test scenarios where perfect squares can be formed by combining set elements"""
    assert sum_perfect_squares_from_set({2, 8}) == 16  # 4 (2*2) is a perfect square
    assert sum_perfect_squares_from_set({3, 12}) == 36  # 36 (3*12) is a perfect square

def test_empty_set():
    """Test empty set"""
    assert sum_perfect_squares_from_set(set()) == 0

def test_no_perfect_squares():
    """Test set with no perfect squares"""
    assert sum_perfect_squares_from_set({5, 7, 11}) == 0

def test_repeated_squares():
    """Test sets with repeated perfect squares"""
    assert sum_perfect_squares_from_set({4, 4, 9}) == 13

def test_negative_numbers():
    """Test sets containing negative numbers"""
    assert sum_perfect_squares_from_set({-4, 4, 9}) == 13
    assert sum_perfect_squares_from_set({-1, -4, 16}) == 16

def test_mix_of_integers():
    """Test set with mixed integers that may form perfect squares"""
    assert sum_perfect_squares_from_set({2, 3, 4, 6}) == 16

def test_invalid_input_types():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        sum_perfect_squares_from_set(123)
    
    with pytest.raises(TypeError):
        sum_perfect_squares_from_set(['a', 'b', 'c'])

def test_input_conversion():
    """Test input conversion and handling"""
    assert sum_perfect_squares_from_set(['4', 9, '16']) == 29
    assert sum_perfect_squares_from_set(('4', 9, '16')) == 29