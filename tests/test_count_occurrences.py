import pytest
from src.count_occurrences import count_element_occurrences

def test_count_basic_occurrences():
    """Test counting occurrences of an element in a simple list."""
    assert count_element_occurrences([1, 2, 3, 2, 2, 4], 2) == 3
    assert count_element_occurrences(['a', 'b', 'a', 'c', 'a'], 'a') == 3

def test_count_no_occurrences():
    """Test when the element does not exist in the list."""
    assert count_element_occurrences([1, 2, 3, 4], 5) == 0
    assert count_element_occurrences([], 1) == 0

def test_count_different_types():
    """Test counting occurrences with different types of elements."""
    assert count_element_occurrences([1, '1', 1, '1'], 1) == 2
    assert count_element_occurrences([1, '1', 1, '1'], '1') == 2

def test_input_validation():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences(123, 1)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences("not a list", 'a')
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences(None, 1)

def test_edge_cases():
    """Test edge cases like empty list, None values, etc."""
    assert count_element_occurrences([None, None, 1, None], None) == 3
    assert count_element_occurrences([1, 2, 3], None) == 0