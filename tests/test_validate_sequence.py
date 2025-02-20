import pytest
from src.validate_sequence import is_valid_increasing_sequence

def test_valid_increasing_sequences():
    # Basic valid sequences
    assert is_valid_increasing_sequence([1, 2, 3]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True
    
def test_empty_and_single_element_sequences():
    # Empty and single element lists are valid
    assert is_valid_increasing_sequence([]) == True
    assert is_valid_increasing_sequence([5]) == True

def test_invalid_sequences():
    # Sequences with duplicate values
    assert is_valid_increasing_sequence([1, 2, 2]) == False
    assert is_valid_increasing_sequence([1, 1, 2]) == False
    
    # Sequences not in strictly increasing order
    assert is_valid_increasing_sequence([3, 2, 1]) == False
    assert is_valid_increasing_sequence([1, 3, 2]) == False
    assert is_valid_increasing_sequence([1, 1, 2, 3]) == False

def test_non_integer_input():
    # Non-integer inputs
    assert is_valid_increasing_sequence([1.5, 2.5, 3.5]) == False
    assert is_valid_increasing_sequence(['a', 'b', 'c']) == False
    assert is_valid_increasing_sequence(None) == False

def test_mixed_type_inputs():
    # Mixed type inputs
    assert is_valid_increasing_sequence([1, 2, '3']) == False