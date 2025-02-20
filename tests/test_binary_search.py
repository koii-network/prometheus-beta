import pytest
from src.binary_search import find_first_occurrence

def test_find_first_occurrence():
    # Test basic cases
    assert find_first_occurrence([1, 2, 3, 4, 5], 3) == 2
    assert find_first_occurrence([1, 2, 2, 2, 3, 4, 5], 2) == 1
    
    # Test first and last elements
    assert find_first_occurrence([1, 2, 3, 4, 5], 1) == 0
    assert find_first_occurrence([1, 2, 3, 4, 5], 5) == 4
    
    # Test multiple occurrences
    assert find_first_occurrence([1, 2, 2, 3, 3, 3, 4, 5], 3) == 3
    
    # Test target not in array
    assert find_first_occurrence([1, 2, 3, 4, 5], 6) == -1
    assert find_first_occurrence([1, 2, 3, 4, 5], 0) == -1
    
    # Test empty array
    assert find_first_occurrence([], 3) == -1
    
    # Large array test
    large_arr = list(range(1, 1001)) + [1001] * 5
    assert find_first_occurrence(large_arr, 1001) == 1000