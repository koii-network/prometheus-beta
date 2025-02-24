import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test basic weighted sum calculation."""
    numbers = [1, 2, 3]
    weights = [0.5, 1, 1.5]
    assert compute_weighted_sum(numbers, weights) == 1*0.5 + 2*1 + 3*1.5

def test_float_inputs():
    """Test weighted sum with float inputs."""
    numbers = [1.5, 2.5, 3.5]
    weights = [0.5, 1.0, 1.5]
    assert compute_weighted_sum(numbers, weights) == 1.5*0.5 + 2.5*1.0 + 3.5*1.5

def test_single_element():
    """Test weighted sum with a single element."""
    numbers = [10]
    weights = [2]
    assert compute_weighted_sum(numbers, weights) == 10 * 2

def test_zero_weights():
    """Test weighted sum with some zero weights."""
    numbers = [1, 2, 3]
    weights = [0, 1, 0]
    assert compute_weighted_sum(numbers, weights) == 2

def test_negative_inputs():
    """Test weighted sum with negative numbers and weights."""
    numbers = [-1, 2, -3]
    weights = [1, -2, 0.5]
    assert compute_weighted_sum(numbers, weights) == -1*1 + 2*(-2) + (-3)*0.5

def test_empty_lists_raise_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="Input lists cannot be empty"):
        compute_weighted_sum([], [])

def test_mismatched_lengths_raise_error():
    """Test that lists with different lengths raise a ValueError."""
    with pytest.raises(ValueError, match="Numbers and weights lists must have the same length"):
        compute_weighted_sum([1, 2], [1, 2, 3])

def test_non_numeric_inputs_raise_error():
    """Test that non-numeric inputs raise a ValueError."""
    with pytest.raises(ValueError):
        compute_weighted_sum([1, 'a'], [1, 2])
    
    with pytest.raises(ValueError):
        compute_weighted_sum([1, 2], [1, '2'])