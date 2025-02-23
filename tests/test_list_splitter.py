import pytest
from src.list_splitter import can_split_list_with_equal_sum

def test_can_split_list_with_equal_sum():
    """Test various scenarios for list splitting"""
    # Positive cases where sum can be split into two equal parts
    assert can_split_list_with_equal_sum([1, 5, 11, 5]) == True
    assert can_split_list_with_equal_sum([1, 2, 3, 4, 5, 6, 7]) == True
    
    # Negative cases where sum cannot be split into two equal parts
    assert can_split_list_with_equal_sum([1, 2, 3, 4, 5]) == False
    
    # Special cases
    assert can_split_list_with_equal_sum([0, 0]) == True
    
    # Potentially ambiguous cases
    # When all elements are the same and total is even, typically considered splittable
    assert can_split_list_with_equal_sum([1, 1, 1, 1]) == True

def test_input_validation():
    """Test input validation"""
    # Non-list input
    with pytest.raises(TypeError):
        can_split_list_with_equal_sum("not a list")
    
    # List with non-integer elements
    with pytest.raises(ValueError):
        can_split_list_with_equal_sum([1, 2, "3", 4])
    
    # List with floating point numbers
    with pytest.raises(ValueError):
        can_split_list_with_equal_sum([1.5, 2.5, 3.0])

def test_complex_cases():
    """Test more complex splitting scenarios"""
    assert can_split_list_with_equal_sum([1, 1, 1, 1, 1, 1, 1, 1]) == True
    # For this specific case, the test expectation might need domain-specific clarification
    # The current implementation considers this splittable