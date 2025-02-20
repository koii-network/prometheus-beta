import pytest
from src.count_matching_elements import count_matching_elements

def test_count_matching_elements():
    # Test basic scenario with matching elements
    assert count_matching_elements([1, 2, 3], [3, 4, 5]) == 1
    
    # Test with multiple matching elements
    assert count_matching_elements([1, 2, 3, 4], [3, 4, 5, 6]) == 2
    
    # Test with no matching elements
    assert count_matching_elements([1, 2], [3, 4]) == 0
    
    # Test with empty arrays
    assert count_matching_elements([], [1, 2, 3]) == 0
    assert count_matching_elements([1, 2, 3], []) == 0
    
    # Test with duplicate elements
    assert count_matching_elements([1, 1, 2], [1, 3]) == 2
    
    # Test with repeated matches
    assert count_matching_elements([1, 1, 2, 2], [1, 2, 3]) == 4