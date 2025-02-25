import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence_length

def test_normal_case():
    """Test a typical case with multiple increasing subsequences."""
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    assert longest_increasing_subsequence_length(arr) == 5

def test_empty_list():
    """Test behavior with an empty list."""
    assert longest_increasing_subsequence_length([]) == 0

def test_single_element():
    """Test with a single element list."""
    assert longest_increasing_subsequence_length([5]) == 1

def test_already_sorted():
    """Test with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert longest_increasing_subsequence_length(arr) == 5

def test_descending_list():
    """Test with a descending list."""
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence_length(arr) == 1

def test_repeated_elements():
    """Test with repeated elements."""
    arr = [3, 3, 3, 3]
    assert longest_increasing_subsequence_length(arr) == 1

def test_mixed_positive_negative():
    """Test with mixed positive and negative numbers."""
    arr = [-1, 3, 0, 2, -5, 4]
    assert longest_increasing_subsequence_length(arr) == 4

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError):
        longest_increasing_subsequence_length("not a list")

def test_invalid_input_non_numeric():
    """Test raising ValueError for non-numeric elements."""
    with pytest.raises(ValueError):
        longest_increasing_subsequence_length([1, 2, "three", 4])

def test_floating_point_numbers():
    """Test with floating point numbers."""
    arr = [1.5, 2.7, 0.5, 3.2, 4.1]
    assert longest_increasing_subsequence_length(arr) == 4