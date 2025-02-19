import pytest
from src.list_split_equal_sum import can_split_list_with_equal_sum

def test_can_split_list_with_equal_sum():
    # Test cases that can be split
    assert can_split_list_with_equal_sum([1, 5, 11, 5]) == True
    assert can_split_list_with_equal_sum([1, 2, 3, 4, 5, 5]) == True
    
    # Test cases that cannot be split
    assert can_split_list_with_equal_sum([1, 2, 3, 5]) == False
    assert can_split_list_with_equal_sum([1, 1, 1, 1, 1, 1, 1, 1]) == False
    
    # Edge cases
    assert can_split_list_with_equal_sum([]) == False
    assert can_split_list_with_equal_sum([1]) == False
    assert can_split_list_with_equal_sum([2, 2]) == True
    
    # Large number case
    assert can_split_list_with_equal_sum([1, 15, 11, 5, 19, 20, 10]) == True
    
    # Negative numbers
    assert can_split_list_with_equal_sum([-1, 1, 0]) == True
    
    # All zeros
    assert can_split_list_with_equal_sum([0, 0, 0, 0]) == True