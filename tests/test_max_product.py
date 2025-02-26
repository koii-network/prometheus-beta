import pytest
from src.max_product import find_max_product

def test_positive_numbers():
    """Test with a list of positive numbers"""
    assert find_max_product([1, 2, 3, 4, 5]) == 20

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers"""
    assert find_max_product([-10, -5, 2, 3, 4]) == 50

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert find_max_product([-5, -2, -1, -10]) == 50

def test_two_numbers():
    """Test with exactly two numbers"""
    assert find_max_product([3, 4]) == 12

def test_large_numbers():
    """Test with large numbers"""
    assert find_max_product([1000, 500, -1000, -500]) == 500000

def test_invalid_input_too_few_numbers():
    """Test raising ValueError when list has fewer than two numbers"""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        find_max_product([1])

def test_invalid_input_not_a_list():
    """Test raising TypeError when input is not a list"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_max_product("not a list")

def test_invalid_input_non_numeric():
    """Test raising TypeError when list contains non-numeric elements"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_max_product([1, 2, 'a', 3])