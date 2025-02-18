import pytest
import math
from src.standard_deviation import calculate_standard_deviation

def test_standard_deviation_normal_case():
    """Test standard deviation for a typical list of numbers"""
    numbers = [2, 4, 4, 4, 5, 5, 7, 9]
    expected = math.sqrt(sum((x - 5)**2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-9)

def test_standard_deviation_single_element():
    """Test standard deviation for a single-element list"""
    numbers = [5]
    assert calculate_standard_deviation(numbers) == 0

def test_standard_deviation_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate standard deviation of an empty list"):
        calculate_standard_deviation([])

def test_standard_deviation_non_numeric():
    """Test that non-numeric inputs raise a TypeError"""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        calculate_standard_deviation([1, 2, 'a', 4])

def test_standard_deviation_mixed_numeric_types():
    """Test that the function works with mixed numeric types"""
    numbers = [1, 2.5, 3, 4]
    result = calculate_standard_deviation(numbers)
    assert isinstance(result, float)
    assert result > 0