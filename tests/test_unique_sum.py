import pytest
from src.unique_sum import sum_unique_elements

def test_basic_unique_sum():
    """Test basic functionality with unique and duplicate elements"""
    assert sum_unique_elements([1, 2, 3, 2]) == 4
    assert sum_unique_elements([1, 1, 1, 1]) == 0
    assert sum_unique_elements([1, 2, 3, 4]) == 10

def test_empty_list():
    """Test with an empty list"""
    assert sum_unique_elements([]) == 0

def test_negative_numbers():
    """Test with negative numbers"""
    assert sum_unique_elements([-1, -2, -1, 3, 3]) == -3

def test_mixed_duplicates():
    """Test with multiple sets of duplicates"""
    assert sum_unique_elements([1, 2, 3, 1, 2, 4]) == 7

def test_type_error_non_list():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_unique_elements("not a list")

def test_type_error_non_integers():
    """Test that list with non-integer elements raises TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, "3", 4])

def test_large_list():
    """Test with a larger list of numbers"""
    large_list = list(range(1000)) + list(range(1000))
    assert sum_unique_elements(large_list) == sum(range(1000))