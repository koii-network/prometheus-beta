import pytest
from src.even_sum import calculate_even_sum

def test_calculate_even_sum_normal_case():
    """Test sum of even numbers in a mixed array"""
    assert calculate_even_sum([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6

def test_calculate_even_sum_all_even():
    """Test sum when all numbers are even"""
    assert calculate_even_sum([2, 4, 6, 8, 10]) == 30

def test_calculate_even_sum_no_even():
    """Test sum when no even numbers are present"""
    assert calculate_even_sum([1, 3, 5, 7]) == 0

def test_calculate_even_sum_empty_list():
    """Test sum of an empty list"""
    assert calculate_even_sum([]) == 0

def test_calculate_even_sum_negative_even():
    """Test sum including negative even numbers"""
    assert calculate_even_sum([-2, -1, 0, 1, 2]) == 0

def test_calculate_even_sum_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        calculate_even_sum("not a list")

def test_calculate_even_sum_invalid_element_type():
    """Test that ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        calculate_even_sum([1, 2, "3", 4])