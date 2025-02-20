import pytest
from src.reorder_integers import reorder_consecutive_integers

def test_valid_reordering():
    # Test cases where reordering is possible
    assert sorted(reorder_consecutive_integers([4, 1, 3, 2])) == [1, 2, 3, 4]
    assert sorted(reorder_consecutive_integers([1, 2, 3, 4])) == [1, 2, 3, 4]
    assert sorted(reorder_consecutive_integers([4, 3, 2, 1])) == [1, 2, 3, 4]

def test_reordering_with_repetitions():
    # Test cases with repeated numbers
    result = reorder_consecutive_integers([1, 1, 2, 2])
    assert result is not None
    assert len(result) == 4
    assert sorted(result) == [1, 1, 2, 2]

def test_impossible_reordering():
    # Test cases where reordering is impossible
    assert reorder_consecutive_integers([1, 10, 100]) is None
    assert reorder_consecutive_integers([5, 7, 9]) is None

def test_edge_cases():
    # Test edge cases
    assert reorder_consecutive_integers([]) == []
    assert len(reorder_consecutive_integers([42])) == 1

def test_consecutive_after_reordering():
    # Ensure the differences between consecutive elements are 0, 1, or -1
    nums = [4, 1, 3, 2]
    result = reorder_consecutive_integers(nums)
    assert result is not None
    
    # Check differences between consecutive elements
    for i in range(1, len(result)):
        diff = abs(result[i] - result[i-1])
        assert diff in [0, 1], f"Invalid difference between {result[i-1]} and {result[i]}"