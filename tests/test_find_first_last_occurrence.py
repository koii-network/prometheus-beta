import pytest
from src.find_first_last_occurrence import find_first_last_occurrence

def test_find_first_last_occurrence():
    # Test with a regular case of multiple occurrences
    assert find_first_last_occurrence([1, 2, 2, 2, 3, 4, 5], 2) == (1, 3)
    
    # Test with a single occurrence
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 3) == (2, 2)
    
    # Test with element at the start
    assert find_first_last_occurrence([1, 1, 1, 2, 3, 4], 1) == (0, 2)
    
    # Test with element at the end
    assert find_first_last_occurrence([1, 2, 3, 4, 5, 5, 5], 5) == (4, 6)
    
    # Test with element not in the array
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 6) == (-1, -1)
    
    # Test with empty array
    assert find_first_last_occurrence([], 1) == (-1, -1)
    
    # Test with single element that matches
    assert find_first_last_occurrence([1], 1) == (0, 0)
    
    # Test with single element that doesn't match
    assert find_first_last_occurrence([1], 2) == (-1, -1)

# Optional: Add a test with a larger array to verify performance
def test_find_first_last_occurrence_large_array():
    large_array = list(range(1000)) + list(range(1000, 2000)) * 2 + list(range(2000, 3000))
    assert find_first_last_occurrence(large_array, 1500) == (1500, 3499)