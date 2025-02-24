import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence_length

def test_typical_sequence():
    """Test a typical sequence with multiple increasing subsequences."""
    assert longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_already_sorted_sequence():
    """Test a sequence that is already sorted in ascending order."""
    assert longest_increasing_subsequence_length([1, 2, 3, 4, 5]) == 5

def test_decreasing_sequence():
    """Test a sequence in descending order."""
    assert longest_increasing_subsequence_length([5, 4, 3, 2, 1]) == 1

def test_empty_list():
    """Test an empty list."""
    assert longest_increasing_subsequence_length([]) == 0

def test_single_element_list():
    """Test a list with a single element."""
    assert longest_increasing_subsequence_length([42]) == 1

def test_duplicate_elements():
    """Test a list with duplicate elements."""
    assert longest_increasing_subsequence_length([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6

def test_mixed_float_int():
    """Test a sequence with mixed float and int types."""
    assert longest_increasing_subsequence_length([1, 2.5, 3, 4.7, 5]) == 5

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        longest_increasing_subsequence_length("not a list")

def test_non_numeric_elements():
    """Test raising ValueError for non-numeric elements."""
    with pytest.raises(ValueError, match="List must contain only numeric elements"):
        longest_increasing_subsequence_length([1, 2, "three", 4])

def test_complex_sequence():
    """Test a more complex sequence with multiple potential subsequences."""
    assert longest_increasing_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6