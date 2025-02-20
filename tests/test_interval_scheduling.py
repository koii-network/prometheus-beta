import pytest
from src.interval_scheduling import max_non_overlapping_intervals

def test_empty_intervals():
    """Test with no intervals"""
    assert max_non_overlapping_intervals([]) == 0

def test_single_interval():
    """Test with a single interval"""
    assert max_non_overlapping_intervals([(1, 3)]) == 1

def test_non_overlapping_intervals():
    """Test with multiple non-overlapping intervals"""
    intervals = [(1, 3), (4, 6), (7, 9)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_overlapping_intervals():
    """Test with overlapping intervals"""
    intervals = [(1, 3), (2, 4), (3, 5)]
    assert max_non_overlapping_intervals(intervals) == 1

def test_complex_overlapping_intervals():
    """Test with a more complex set of overlapping intervals"""
    intervals = [(1, 3), (2, 5), (3, 7), (4, 6), (6, 8)]
    assert max_non_overlapping_intervals(intervals) == 2

def test_touch_point_intervals():
    """Test intervals that touch at their endpoints"""
    intervals = [(1, 3), (3, 5), (5, 7)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_invalid_interval():
    """Test raising error for invalid intervals"""
    with pytest.raises(ValueError, match="Invalid interval"):
        max_non_overlapping_intervals([(5, 3)])

def test_equal_start_end_time():
    """Test intervals with equal start and end times"""
    intervals = [(1, 1), (2, 2), (3, 3)]
    assert max_non_overlapping_intervals(intervals) == 3