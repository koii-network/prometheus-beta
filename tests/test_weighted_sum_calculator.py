import pytest
from src.weighted_sum_calculator import calculate_weighted_sum

def test_basic_weighted_sum():
    """Test basic weighted sum calculation"""
    numbers = [1, 2, 3]
    weights = [0.5, 0.3, 0.2]
    result = calculate_weighted_sum(numbers, weights)
    assert result == pytest.approx(1 * 0.5 + 2 * 0.3 + 3 * 0.2)

def test_integer_weighted_sum():
    """Test weighted sum with integer weights"""
    numbers = [10, 20, 30]
    weights = [1, 2, 3]
    result = calculate_weighted_sum(numbers, weights)
    assert result == pytest.approx(10 * 1 + 20 * 2 + 30 * 3)

def test_different_length_lists_raises_error():
    """Test that different length lists raise a ValueError"""
    with pytest.raises(ValueError, match="Number of numbers and weights must be equal"):
        calculate_weighted_sum([1, 2], [0.5])

def test_non_numeric_numbers_raises_error():
    """Test that non-numeric numbers raise a TypeError"""
    with pytest.raises(TypeError, match="Numbers must be numeric"):
        calculate_weighted_sum(['a', 'b'], [1, 2])

def test_non_numeric_weights_raises_error():
    """Test that non-numeric weights raise a TypeError"""
    with pytest.raises(TypeError, match="Weights must be numeric"):
        calculate_weighted_sum([1, 2], ['x', 'y'])

def test_non_list_inputs_raises_error():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        calculate_weighted_sum(1, 2)

def test_empty_lists():
    """Test weighted sum with empty lists"""
    result = calculate_weighted_sum([], [])
    assert result == 0