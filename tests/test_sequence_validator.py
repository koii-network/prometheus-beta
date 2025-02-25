import pytest
from src.sequence_validator import is_valid_increasing_sequence

def test_valid_increasing_sequence():
    """Test valid strictly increasing sequences"""
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True

def test_single_element_sequence():
    """Test single element sequence"""
    assert is_valid_increasing_sequence([42]) == True
    assert is_valid_increasing_sequence([-5]) == True

def test_empty_sequence():
    """Test empty sequence"""
    assert is_valid_increasing_sequence([]) == True

def test_invalid_increasing_sequence():
    """Test sequences that are not strictly increasing"""
    assert is_valid_increasing_sequence([1, 2, 2, 3]) == False
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False
    assert is_valid_increasing_sequence([1, 3, 2, 4]) == False

def test_input_with_non_integers():
    """Test input with non-integer elements"""
    assert is_valid_increasing_sequence(['a', 'b', 'c']) == False
    assert is_valid_increasing_sequence([1, 2, '3']) == False

def test_input_type_error():
    """Test input type other than list"""
    with pytest.raises(TypeError):
        is_valid_increasing_sequence("not a list")
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(123)
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(None)