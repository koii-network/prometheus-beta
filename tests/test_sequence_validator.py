import pytest
from src.sequence_validator import is_valid_increasing_sequence

def test_valid_increasing_sequence():
    """Test a valid increasing sequence of integers"""
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True

def test_valid_increasing_sequence_with_large_numbers():
    """Test a valid increasing sequence with larger numbers"""
    assert is_valid_increasing_sequence([10, 20, 30, 40, 50]) == True

def test_invalid_sequence_not_increasing():
    """Test a sequence that is not strictly increasing"""
    assert is_valid_increasing_sequence([1, 2, 2, 3, 4]) == False

def test_invalid_sequence_decreasing():
    """Test a decreasing sequence"""
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False

def test_invalid_sequence_duplicate_elements():
    """Test a sequence with duplicate elements"""
    assert is_valid_increasing_sequence([1, 2, 3, 3, 4]) == False

def test_single_element_sequence():
    """Test a single element sequence"""
    assert is_valid_increasing_sequence([42]) == True

def test_empty_sequence():
    """Test an empty sequence"""
    assert is_valid_increasing_sequence([]) == False

def test_non_integer_sequence():
    """Test a sequence with non-integer elements"""
    assert is_valid_increasing_sequence([1, 2.5, 3, 4]) == False

def test_non_list_input():
    """Test non-list input"""
    assert is_valid_increasing_sequence("not a list") == False
    assert is_valid_increasing_sequence(123) == False
    assert is_valid_increasing_sequence(None) == False