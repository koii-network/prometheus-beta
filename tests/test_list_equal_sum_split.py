import pytest
from src.list_equal_sum_split import can_split_list_equally

def test_can_split_list_equally():
    # Test cases that can be split equally
    assert can_split_list_equally([1, 5, 11, 5]) == True
    assert can_split_list_equally([1, 2, 3, 5]) == False
    
    # Edge cases
    assert can_split_list_equally([]) == False
    assert can_split_list_equally([10]) == False
    
    # More test cases
    assert can_split_list_equally([1, 1, 1, 1]) == True
    assert can_split_list_equally([3, 3, 3, 3]) == True
    assert can_split_list_equally([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_split_list_equally([1, 2, 3, 4, 5, 6]) == False
    
    # Large number case
    assert can_split_list_equally([100, 100, 100, 100, 100, 100]) == True
    
    # Negative numbers
    assert can_split_list_equally([-1, 1, 0]) == True
    assert can_split_list_equally([-5, 5, 10, -10]) == True