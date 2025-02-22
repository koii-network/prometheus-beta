import pytest
from src.sequence_validator import is_valid_sequence

def test_valid_increasing_sequence():
    """Test a valid strictly increasing sequence"""
    assert is_valid_sequence([1, 2, 3, 4, 5]) == True

def test_empty_sequence():
    """Test an empty sequence"""
    assert is_valid_sequence([]) == True

def test_single_element_sequence():
    """Test a single element sequence"""
    assert is_valid_sequence([42]) == True

def test_invalid_non_increasing_sequence():
    """Test a sequence that is not strictly increasing"""
    assert is_valid_sequence([1, 2, 2, 3]) == False
    assert is_valid_sequence([5, 4, 3, 2, 1]) == False
    assert is_valid_sequence([1, 3, 2, 4]) == False

def test_invalid_repeated_elements():
    """Test a sequence with repeated elements"""
    assert is_valid_sequence([1, 1, 2, 3]) == False
    assert is_valid_sequence([1, 2, 2, 3]) == False

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        is_valid_sequence("not a list")
    with pytest.raises(TypeError):
        is_valid_sequence(123)

def test_mixed_type_elements():
    """Test a sequence with non-integer elements"""
    assert is_valid_sequence([1, 2, 3, 'a']) == False