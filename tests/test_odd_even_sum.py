import pytest
from src.odd_even_sum import calculate_odd_even_sum

def test_mixed_numbers():
    """Test with a mix of odd and even numbers"""
    result = calculate_odd_even_sum([1, 2, 3, 4, 5, 6])
    assert result == (9, 12)  # Odd sum: 1+3+5, Even sum: 2+4+6

def test_only_even_numbers():
    """Test with only even numbers"""
    result = calculate_odd_even_sum([2, 4, 6, 8])
    assert result == (0, 20)

def test_only_odd_numbers():
    """Test with only odd numbers"""
    result = calculate_odd_even_sum([1, 3, 5, 7])
    assert result == (16, 0)

def test_empty_list():
    """Test with an empty list"""
    result = calculate_odd_even_sum([])
    assert result == (0, 0)

def test_zero_and_negative_numbers():
    """Test with zero and negative numbers"""
    result = calculate_odd_even_sum([-1, 0, 1, -2, 2])
    assert result == (0, 0)

def test_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_odd_even_sum("not a list")

def test_invalid_element_type():
    """Test with list containing non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        calculate_odd_even_sum([1, 2, "3", 4])