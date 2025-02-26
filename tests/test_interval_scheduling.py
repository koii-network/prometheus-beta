import pytest
from src.interval_scheduling import max_non_overlapping_intervals

def test_empty_intervals():
    """Test handling of empty interval list."""
    assert max_non_overlapping_intervals([]) == 0

def test_single_interval():
    """Test with a single interval."""
    assert max_non_overlapping_intervals([(1, 3)]) == 1

def test_non_overlapping_intervals():
    """Test intervals that do not overlap."""
    intervals = [(1, 2), (3, 4), (5, 6)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_overlapping_intervals():
    """Test intervals with some overlaps."""
    intervals = [(1, 3), (2, 4), (3, 5), (6, 7)]
    assert max_non_overlapping_intervals(intervals) == 2

def test_complex_overlapping_intervals():
    """Test a more complex scenario of overlapping intervals."""
    intervals = [(1, 3), (2, 4), (3, 5), (5, 7), (6, 8), (8, 10)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_edge_case_same_start_end():
    """Test intervals with same start and end time."""
    intervals = [(1, 1), (2, 2), (3, 3)]
    assert max_non_overlapping_intervals(intervals) == 3

def test_invalid_interval_raises_error():
    """Test that invalid intervals (end < start) raise a ValueError."""
    with pytest.raises(ValueError, match="Invalid interval"):
        max_non_overlapping_intervals([(3, 1)])

def test_mixed_interval_sizes():
    """Test intervals of various sizes."""
    intervals = [(1, 10), (2, 3), (4, 5), (6, 7), (8, 9)]
    assert max_non_overlapping_intervals(intervals) == 4