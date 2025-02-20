import pytest
from src.weighted_sum import compute_weighted_sum

def test_compute_weighted_sum_basic():
    """Test basic weighted sum calculation"""
    numbers = [1, 2, 3]
    weights = [0.5, 0.3, 0.2]
    result = compute_weighted_sum(numbers, weights)
    assert result == pytest.approx(1.7)  # (1*0.5) + (2*0.3) + (3*0.2)

def test_compute_weighted_sum_integers():
    """Test weighted sum with integer weights"""
    numbers = [10, 20, 30]
    weights = [1, 2, 3]
    result = compute_weighted_sum(numbers, weights)
    assert result == 140  # (10*1) + (20*2) + (30*3)

def test_compute_weighted_sum_empty_lists():
    """Test weighted sum with empty lists"""
    numbers = []
    weights = []
    result = compute_weighted_sum(numbers, weights)
    assert result == 0

def test_compute_weighted_sum_mismatched_lengths():
    """Test that an error is raised when list lengths do not match"""
    numbers = [1, 2, 3]
    weights = [0.5, 0.3]
    with pytest.raises(ValueError, match="The number of elements in 'numbers' and 'weights' must be the same"):
        compute_weighted_sum(numbers, weights)

def test_compute_weighted_sum_zero_weights():
    """Test weighted sum with zero weights"""
    numbers = [5, 10, 15]
    weights = [0, 0, 0]
    result = compute_weighted_sum(numbers, weights)
    assert result == 0

def test_compute_weighted_sum_negative_values():
    """Test weighted sum with negative numbers and weights"""
    numbers = [-1, 2, -3]
    weights = [0.5, -0.3, 0.2]
    result = compute_weighted_sum(numbers, weights)
    assert result == pytest.approx(-1.7)  # (-1*0.5) + (2*-0.3) + (-3*0.2)