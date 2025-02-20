import pytest
from src.weighted_sum import compute_weighted_sum

def test_basic_weighted_sum():
    """Test a basic weighted sum calculation."""
    numbers = [1, 2, 3]
    weights = [0.5, 0.3, 0.2]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(1.8)

def test_single_element():
    """Test weighted sum with a single element."""
    numbers = [5]
    weights = [1]
    assert compute_weighted_sum(numbers, weights) == 5

def test_negative_numbers():
    """Test weighted sum with negative numbers and weights."""
    numbers = [-1, 2, -3]
    weights = [0.5, 0.3, 0.2]
    assert compute_weighted_sum(numbers, weights) == pytest.approx(-1.8)

def test_zero_weight():
    """Test weighted sum with zero weights."""
    numbers = [1, 2, 3]
    weights = [0, 0, 0]
    assert compute_weighted_sum(numbers, weights) == 0

def test_empty_lists_raise_error():
    """Test that empty lists raise a ValueError."""
    with pytest.raises(ValueError, match="Both numbers and weights lists must be non-empty"):
        compute_weighted_sum([], [])

def test_mismatched_lengths_raise_error():
    """Test that lists of different lengths raise a ValueError."""
    with pytest.raises(ValueError, match="Numbers and weights lists must have the same length"):
        compute_weighted_sum([1, 2], [0.5])