import pytest
from src.longest_consecutive_sequence import find_longest_consecutive_sequence

def test_standard_case():
    """Test a standard list with a clear consecutive sequence."""
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_empty_list():
    """Test an empty list returns an empty list."""
    assert find_longest_consecutive_sequence([]) == []

def test_no_consecutive_sequence():
    """Test a list with no consecutive numbers."""
    assert find_longest_consecutive_sequence([5, 10, 15, 20]) == [5]

def test_multiple_equal_length_sequences():
    """Test when multiple sequences of same length exist."""
    result = find_longest_consecutive_sequence([1, 2, 3, 10, 11, 12])
    assert result in [[1, 2, 3], [10, 11, 12]]

def test_duplicate_numbers():
    """Test a list with duplicate numbers."""
    assert find_longest_consecutive_sequence([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]

def test_single_number():
    """Test a list with a single number."""
    assert find_longest_consecutive_sequence([42]) == [42]

def test_negative_numbers():
    """Test a list with negative numbers."""
    assert find_longest_consecutive_sequence([-5, -4, -3, 1, 2, 3]) == [-5, -4, -3]