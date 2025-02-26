import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test basic weighted sum calculation."""
    numbers = [1, 2, 3]
    weights = [0.5, 0.3, 0.2]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(1.8)

def test_single_element_weighted_sum():
    """Test weighted sum with a single element."""
    numbers = [10]
    weights = [1]
    assert compute_weighted_sum(numbers, weights) == 10

def test_zero_weights():
    """Test weighted sum with some zero weights."""
    numbers = [1, 2, 3]
    weights = [0, 1, 0]
    assert compute_weighted_sum(numbers, weights) == 2

def test_negative_numbers_and_weights():
    """Test weighted sum with negative numbers and weights."""
    numbers = [-1, 2, -3]
    weights = [0.5, -0.3, 0.2]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(-1.3)

def test_float_numbers():
    """Test weighted sum with float numbers."""
    numbers = [1.5, 2.5, 3.5]
    weights = [0.1, 0.2, 0.3]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(2.5)

def test_empty_lists_raise_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="Input lists cannot be empty"):
        compute_weighted_sum([], [])

def test_mismatched_list_lengths_raise_error():
    """Test that lists of different lengths raise a ValueError."""
    with pytest.raises(ValueError, match="Lists of numbers and weights must have the same length"):
        compute_weighted_sum([1, 2], [0.5])

def test_non_numeric_inputs_raise_error():
    """Test that non-numeric inputs raise a TypeError."""
    with pytest.raises(TypeError, match="All numbers and weights must be numeric"):
        compute_weighted_sum([1, 'a'], [0.5, 0.5])
    
    with pytest.raises(TypeError, match="All numbers and weights must be numeric"):
        compute_weighted_sum([1, 2], [0.5, 'b'])