import pytest
from src.longest_increasing_subsequence import find_lis_length

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    assert find_lis_length([10, 22, 33, 44]) == 4

def test_partially_increasing_sequence():
    """Test a sequence with mixed increasing subsequences"""
    assert find_lis_length([10, 22, 9, 33, 21, 50, 41, 60]) == 5

def test_empty_list():
    """Test an empty list"""
    assert find_lis_length([]) == 0

def test_single_element_list():
    """Test a list with a single element"""
    assert find_lis_length([5]) == 1

def test_repeated_elements():
    """Test a list with repeated elements"""
    assert find_lis_length([5, 5, 5, 5]) == 1

def test_decreasing_sequence():
    """Test a decreasing sequence"""
    assert find_lis_length([7, 6, 5, 4, 3]) == 1

def test_non_consecutive_increasing_sequence():
    """Test a non-consecutive increasing subsequence"""
    assert find_lis_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_type_error_non_list():
    """Test input type validation"""
    with pytest.raises(TypeError):
        find_lis_length("not a list")

def test_value_error_non_numeric():
    """Test numeric element validation"""
    with pytest.raises(ValueError):
        find_lis_length([1, 2, '3', 4])