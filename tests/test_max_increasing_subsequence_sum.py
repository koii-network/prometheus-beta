import pytest
from src.max_increasing_subsequence_sum import max_increasing_subsequence_sum

def test_basic_increasing_sequence():
    """Test a basic increasing sequence."""
    arr = [1, 101, 2, 3, 100]
    assert max_increasing_subsequence_sum(arr) == 106

def test_more_complex_sequence():
    """Test a more complex sequence with multiple possible subsequences."""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert max_increasing_subsequence_sum(arr) == 165

def test_single_element():
    """Test a sequence with a single element."""
    arr = [5]
    assert max_increasing_subsequence_sum(arr) == 5

def test_all_descending():
    """Test a descending sequence."""
    arr = [5, 4, 3, 2, 1]
    assert max_increasing_subsequence_sum(arr) == 5

def test_mixed_sequence():
    """Test a mixed sequence with both positive and negative numbers."""
    arr = [-2, 10, 3, 4, -5, 6, 7]
    assert max_increasing_subsequence_sum(arr) == 20

def test_empty_sequence():
    """Test an empty sequence."""
    arr = []
    assert max_increasing_subsequence_sum(arr) is None

def test_all_same_numbers():
    """Test a sequence with all same numbers."""
    arr = [3, 3, 3, 3]
    assert max_increasing_subsequence_sum(arr) == 3

def test_alternating_numbers():
    """Test an alternating sequence."""
    arr = [1, -1, 2, -2, 3, -3]
    assert max_increasing_subsequence_sum(arr) == 6