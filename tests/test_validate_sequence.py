import pytest
from src.validate_sequence import is_valid_distinct_increasing_sequence

def test_valid_sequences():
    # Test strictly increasing sequences
    assert is_valid_distinct_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_distinct_increasing_sequence([-3, -2, 0, 5, 10]) == True

def test_invalid_sequences():
    # Test non-increasing sequences
    assert is_valid_distinct_increasing_sequence([5, 4, 3, 2, 1]) == False
    assert is_valid_distinct_increasing_sequence([1, 1, 2, 3, 4]) == False
    assert is_valid_distinct_increasing_sequence([1, 2, 2, 3, 4]) == False
    assert is_valid_distinct_increasing_sequence([1, 3, 2, 4, 5]) == False

def test_edge_cases():
    # Test empty list and single element list
    assert is_valid_distinct_increasing_sequence([]) == True
    assert is_valid_distinct_increasing_sequence([42]) == True

def test_invalid_input_types():
    # Test non-list inputs
    with pytest.raises(TypeError):
        is_valid_distinct_increasing_sequence("not a list")
    with pytest.raises(TypeError):
        is_valid_distinct_increasing_sequence(123)
    with pytest.raises(TypeError):
        is_valid_distinct_increasing_sequence(None)

def test_mixed_types():
    # Test sequences with non-integer elements
    assert is_valid_distinct_increasing_sequence([1, 2, 3.0, 4, 5]) == False
    assert is_valid_distinct_increasing_sequence([1, '2', 3, 4, 5]) == False