import pytest
from src.interval_scheduling import max_non_overlapping_intervals

def test_empty_intervals():
    """Test handling of empty interval list"""
    assert max_non_overlapping_intervals([]) == 0

def test_single_interval():
    """Test with a single interval"""
    assert max_non_overlapping_intervals([(1, 3)]) == 1

def test_non_overlapping_intervals():
    """Test intervals that do not overlap"""
    intervals = [(1, 2), (3, 4), (5, 6)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_overlapping_intervals():
    """Test intervals with some overlaps"""
    intervals = [(1, 3), (2, 4), (3, 5), (6, 7)]
    assert max_non_overlapping_intervals(intervals) == 2

def test_complex_overlapping_intervals():
    """Test a more complex scenario with multiple overlaps"""
    intervals = [(1, 3), (2, 4), (3, 5), (4, 6), (6, 7), (8, 10)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_invalid_interval_start_greater_than_end():
    """Test that an error is raised for invalid intervals"""
    with pytest.raises(ValueError, match="Invalid interval"):
        max_non_overlapping_intervals([(3, 1)])

def test_equal_start_end_times():
    """Test intervals with equal start and end times"""
    intervals = [(1, 1), (2, 2), (3, 3)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_completely_nested_intervals():
    """Test scenario with completely nested intervals"""
    intervals = [(1, 10), (2, 3), (4, 5), (6, 7)]
    assert max_non_overlapping_intervals(intervals) == 1

def test_multiple_valid_max_interval_selections():
    """Test scenario where multiple max interval selections are possible"""
    intervals = [(1, 3), (2, 4), (3, 5), (4, 6)]
    assert max_non_overlapping_intervals(intervals) == 2