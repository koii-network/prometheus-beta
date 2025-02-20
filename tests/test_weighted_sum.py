import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test basic weighted sum calculation"""
    numbers = [1, 2, 3]
    weights = [0.5, 0.3, 0.2]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(1.8)

def test_single_element_weighted_sum():
    """Test weighted sum with a single element"""
    numbers = [10]
    weights = [1]
    assert compute_weighted_sum(numbers, weights) == 10

def test_zero_weights():
    """Test weighted sum with some zero weights"""
    numbers = [1, 2, 3]
    weights = [0, 1, 0]
    assert compute_weighted_sum(numbers, weights) == 2

def test_negative_values():
    """Test weighted sum with negative numbers and weights"""
    numbers = [-1, 2, -3]
    weights = [0.5, -0.2, 0.7]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(-2.3)

def test_mismatched_lengths_raises_error():
    """Test that mismatched list lengths raise a ValueError"""
    numbers = [1, 2, 3]
    weights = [0.1, 0.2]
    with pytest.raises(ValueError, match="must have the same length"):
        compute_weighted_sum(numbers, weights)

def test_non_numeric_input_raises_error():
    """Test that non-numeric inputs raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        compute_weighted_sum([1, 'a'], [0.5, 0.5])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="must be lists"):
        compute_weighted_sum(10, [1, 2])