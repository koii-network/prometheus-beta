import pytest
from src.count_difference_five_pairs import count_difference_five_pairs

def test_count_difference_five_pairs():
    # Test cases with pairs having a difference of 5
    assert count_difference_five_pairs([1, 6, 3, 8, 2, 7]) == 2
    
    # Test case with no pairs having a difference of 5
    assert count_difference_five_pairs([1, 2, 3, 4, 5]) == 0
    
    # Test with an empty list
    assert count_difference_five_pairs([]) == 0
    
    # Test with a single element list
    assert count_difference_five_pairs([1]) == 0
    
    # Test with pairs using positive and negative numbers
    assert count_difference_five_pairs([-1, 4, 9, 0, 5]) == 2
    
    # Test with repeated numbers
    assert count_difference_five_pairs([5, 10, 5, 10, 5]) == 2