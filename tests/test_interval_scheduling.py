import pytest
from src.interval_scheduling import max_parallel_intervals

def test_max_parallel_intervals_basic():
    """Test basic scenario with multiple intervals."""
    intervals = [(1, 3), (2, 4), (3, 5), (7, 9)]
    assert max_parallel_intervals(intervals) == 2

def test_max_parallel_intervals_empty():
    """Test empty list of intervals."""
    assert max_parallel_intervals([]) == 0

def test_max_parallel_intervals_single():
    """Test single interval."""
    assert max_parallel_intervals([(1, 5)]) == 1

def test_max_parallel_intervals_no_overlap():
    """Test intervals with no overlap."""
    intervals = [(1, 2), (3, 4), (5, 6)]
    assert max_parallel_intervals(intervals) == 1

def test_max_parallel_intervals_full_overlap():
    """Test intervals with full overlap."""
    intervals = [(1, 5), (2, 4), (3, 4)]
    assert max_parallel_intervals(intervals) == 3

def test_max_parallel_intervals_invalid_interval():
    """Test raising ValueError for invalid intervals."""
    with pytest.raises(ValueError, match="Invalid interval"):
        max_parallel_intervals([(5, 3)])

def test_max_parallel_intervals_complex_scenario():
    """Test a more complex scenario with multiple overlaps."""
    intervals = [(1, 4), (2, 5), (3, 6), (4, 7), (5, 8)]
    assert max_parallel_intervals(intervals) == 3

def test_max_parallel_intervals_same_start_times():
    """Test intervals with same start times."""
    intervals = [(1, 3), (1, 4), (1, 5)]
    assert max_parallel_intervals(intervals) == 3