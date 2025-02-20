import pytest
from src.max_product import max_product_of_two_numbers

def test_positive_numbers():
    """Test with a list of positive numbers"""
    numbers = [1, 2, 3, 4, 5]
    assert max_product_of_two_numbers(numbers) == 20  # 5 * 4

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers"""
    numbers = [-10, -5, 2, 3, 4]
    assert max_product_of_two_numbers(numbers) == 50  # -10 * -5

def test_negative_numbers():
    """Test with a list of negative numbers"""
    numbers = [-3, -4, -1, -2]
    assert max_product_of_two_numbers(numbers) == 12  # -3 * -4

def test_exact_two_numbers():
    """Test with exactly two numbers"""
    numbers = [5, 10]
    assert max_product_of_two_numbers(numbers) == 50

def test_duplicate_numbers():
    """Test with duplicate numbers"""
    numbers = [3, 3, 4, 2]
    assert max_product_of_two_numbers(numbers) == 12  # 3 * 4

def test_too_few_numbers():
    """Test error when list is too short"""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_product_of_two_numbers([1])

def test_empty_list():
    """Test error with empty list"""
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        max_product_of_two_numbers([])