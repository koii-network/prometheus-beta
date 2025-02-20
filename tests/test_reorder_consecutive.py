import pytest
from src.reorder_consecutive import reorder_consecutive_diff

def test_consecutive_reorder_basic():
    # Basic cases where reordering is possible
    assert sorted(reorder_consecutive_diff([1, 2, 3, 4])) == sorted([1, 2, 3, 4])
    assert sorted(reorder_consecutive_diff([4, 3, 2, 1])) == sorted([1, 2, 3, 4])

def test_consecutive_reorder_with_gaps():
    # Test with small differences allowed
    result = reorder_consecutive_diff([1, 3, 5, 4, 2])
    assert result is not None
    assert all(abs(result[i] - result[i+1]) <= 1 for i in range(len(result)-1))

def test_consecutive_reorder_impossible():
    # Test cases where reordering is impossible
    assert reorder_consecutive_diff([1, 10, 20, 30]) is None

def test_consecutive_reorder_edge_cases():
    # Empty list
    assert reorder_consecutive_diff([]) == []
    
    # Single element
    assert reorder_consecutive_diff([5]) == [5]

def test_consecutive_reorder_complex():
    # More complex case
    result = reorder_consecutive_diff([7, 6, 8, 5, 9])
    assert result is not None
    assert set(result) == {5, 6, 7, 8, 9}
    assert all(abs(result[i] - result[i+1]) <= 1 for i in range(len(result)-1))

def test_consecutive_reorder_repeated_elements():
    # Test with repeated elements
    result = reorder_consecutive_diff([1, 1, 2, 2, 3])
    assert result is not None
    assert set(result) == {1, 1, 2, 2, 3}
    assert all(abs(result[i] - result[i+1]) <= 1 for i in range(len(result)-1))