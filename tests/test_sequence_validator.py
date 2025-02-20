import pytest
from src.sequence_validator import is_valid_increasing_sequence

def test_valid_increasing_sequence():
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True

def test_invalid_increasing_sequence():
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False  # Decreasing
    assert is_valid_increasing_sequence([1, 1, 2, 3, 4]) == False  # Duplicates
    assert is_valid_increasing_sequence([1, 3, 2, 4]) == False  # Not strictly increasing

def test_edge_cases():
    assert is_valid_increasing_sequence([42]) == True  # Single element
    assert is_valid_increasing_sequence([]) == False  # Empty list
    assert is_valid_increasing_sequence(None) == False  # None input

def test_non_integer_inputs():
    assert is_valid_increasing_sequence([1.5, 2.5, 3.5]) == False  # Floats
    assert is_valid_increasing_sequence(['a', 'b', 'c']) == False  # Strings
    assert is_valid_increasing_sequence([1, 'a', 3]) == False  # Mixed types