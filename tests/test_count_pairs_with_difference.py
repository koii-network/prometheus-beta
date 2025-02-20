import pytest
from src.count_pairs_with_difference import count_pairs_with_difference_of_five

def test_count_pairs_with_difference_of_five():
    # Test cases with pairs having difference of 5
    assert count_pairs_with_difference_of_five([1, 6, 3, 8, 9, 4]) == 2
    assert count_pairs_with_difference_of_five([1, 6, 2, 7, 3, 8]) == 3
    
    # Test cases with no pairs having difference of 5
    assert count_pairs_with_difference_of_five([1, 2, 3, 4, 5]) == 0
    assert count_pairs_with_difference_of_five([10, 11, 12, 13]) == 0
    
    # Edge cases
    assert count_pairs_with_difference_of_five([]) == 0
    assert count_pairs_with_difference_of_five([1]) == 0
    
    # Test with negative numbers
    assert count_pairs_with_difference_of_five([-1, 4, -6, -1, 3]) == 2