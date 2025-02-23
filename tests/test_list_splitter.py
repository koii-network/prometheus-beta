import pytest
from src.list_splitter import can_split_list_with_equal_sum

def test_can_split_list_with_equal_sum():
    """Test various scenarios for list splitting"""
    # Positive cases
    assert can_split_list_with_equal_sum([1, 5, 11, 5]) == True
    assert can_split_list_with_equal_sum([1, 2, 3, 4, 5, 6, 7]) == True
    
    # Negative cases
    assert can_split_list_with_equal_sum([1, 2, 3, 4, 5]) == False
    assert can_split_list_with_equal_sum([1, 1, 1, 1]) == False
    
    # Edge cases
    assert can_split_list_with_equal_sum([]) == False
    assert can_split_list_with_equal_sum([10]) == False
    assert can_split_list_with_equal_sum([0, 0]) == True

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
    assert can_split_list_with_equal_sum([23, 45, 12, 56, 98, 11, 32]) == True
    assert can_split_list_with_equal_sum([10, 10, 10, 10, 10, 10, 10, 30]) == True