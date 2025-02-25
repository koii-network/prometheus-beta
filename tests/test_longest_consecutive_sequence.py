import pytest
from src.longest_consecutive_sequence import find_longest_consecutive_sequence

def test_basic_sequence():
    """Test a basic consecutive sequence."""
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_longer_sequence():
    """Test a longer consecutive sequence."""
    assert find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_empty_list():
    """Test empty input list."""
    assert find_longest_consecutive_sequence([]) == []

def test_single_element():
    """Test list with a single element."""
    assert find_longest_consecutive_sequence([42]) == [42]

def test_negative_numbers():
    """Test consecutive sequence with negative numbers."""
    assert find_longest_consecutive_sequence([-3, -2, -1, 0, 1, 3, 4, 5]) == [-3, -2, -1, 0, 1]

def test_duplicate_numbers():
    """Test list with duplicate numbers."""
    assert find_longest_consecutive_sequence([1, 2, 2, 3, 3, 4, 5, 5]) == [1, 2, 3, 4, 5]

def test_no_consecutive_sequence():
    """Test list with no consecutive sequence."""
    assert find_longest_consecutive_sequence([9, 1, 4, 7, 3]) == [9]

def test_multiple_same_length_sequences():
    """Test when multiple sequences of the same length exist."""
    result = find_longest_consecutive_sequence([1, 2, 3, 10, 11, 12, 13])
    assert result in [[1, 2, 3], [10, 11, 12, 13]]

def test_large_range():
    """Test a large range of consecutive numbers."""
    large_list = list(range(1000, 2000)) + [500, 501, 502]
    result = find_longest_consecutive_sequence(large_list)
    assert result == list(range(1000, 2000))