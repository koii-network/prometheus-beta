import pytest
from src.increasing_sequence_validator import is_valid_increasing_sequence

def test_valid_increasing_sequence():
    """Test valid increasing sequences"""
    assert is_valid_increasing_sequence([1, 2, 3, 4, 5]) == True
    assert is_valid_increasing_sequence([10, 20, 30, 40]) == True

def test_invalid_increasing_sequence():
    """Test invalid sequences"""
    # Decreasing sequence
    assert is_valid_increasing_sequence([5, 4, 3, 2, 1]) == False
    # Non-increasing sequence
    assert is_valid_increasing_sequence([1, 2, 2, 3, 4]) == False
    # Duplicate elements
    assert is_valid_increasing_sequence([1, 2, 2, 3]) == False

def test_edge_cases():
    """Test edge cases"""
    # Empty list
    assert is_valid_increasing_sequence([]) == True
    # Single element list
    assert is_valid_increasing_sequence([1]) == True
    # Sequence with negative numbers
    assert is_valid_increasing_sequence([-5, -4, -3, -2, -1]) == True

def test_invalid_inputs():
    """Test invalid input types"""
    # Non-list input
    with pytest.raises(TypeError):
        is_valid_increasing_sequence(123)
    
    # List with non-integer elements
    with pytest.raises(ValueError):
        is_valid_increasing_sequence([1, 2, 'a', 3])
    
    # List with mixed types
    with pytest.raises(ValueError):
        is_valid_increasing_sequence([1, 2, 3.5, 4])

def test_type_conversion():
    """Test type conversion of input"""
    assert is_valid_increasing_sequence(['1', '2', '3']) == True
    assert is_valid_increasing_sequence([1.0, 2.0, 3.0]) == True