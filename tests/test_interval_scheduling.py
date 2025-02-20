import pytest
from src.interval_scheduling import max_non_overlapping_intervals

def test_empty_intervals():
    """Test with empty list of intervals"""
    assert max_non_overlapping_intervals([]) == 0

def test_single_interval():
    """Test with a single interval"""
    assert max_non_overlapping_intervals([[1, 3]]) == 1

def test_non_overlapping_intervals():
    """Test with non-overlapping intervals"""
    intervals = [[1, 2], [3, 4], [5, 6]]
    assert max_non_overlapping_intervals(intervals) == 3

def test_overlapping_intervals():
    """Test with overlapping intervals"""
    intervals = [[1, 3], [2, 4], [3, 5], [4, 6]]
    assert max_non_overlapping_intervals(intervals) == 2

def test_complex_overlapping_intervals():
    """Test with a more complex set of overlapping intervals"""
    intervals = [[1, 3], [2, 5], [4, 7], [6, 8], [8, 10]]
    assert max_non_overlapping_intervals(intervals) == 3

def test_invalid_intervals():
    """Test with invalid interval formats"""
    with pytest.raises(ValueError):
        max_non_overlapping_intervals([[3, 2]])  # start > end
    
    with pytest.raises(ValueError):
        max_non_overlapping_intervals([['a', 'b']])  # non-numeric
    
    with pytest.raises(ValueError):
        max_non_overlapping_intervals(None)  # None input

def test_duplicate_intervals():
    """Test with duplicate intervals"""
    intervals = [[1, 3], [1, 3], [1, 3]]
    assert max_non_overlapping_intervals(intervals) == 1

def test_floating_point_intervals():
    """Test with floating-point intervals"""
    intervals = [[1.5, 2.7], [2.8, 3.9], [4.0, 5.2]]
    assert max_non_overlapping_intervals(intervals) == 3