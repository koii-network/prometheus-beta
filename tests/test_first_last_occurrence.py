import pytest
from src.first_last_occurrence import find_first_last_occurrence

def test_find_first_last_occurrence():
    # Test basic case with multiple occurrences
    assert find_first_last_occurrence([1, 2, 2, 2, 3, 4, 5], 2) == (1, 3)
    
    # Test single occurrence
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 3) == (2, 2)
    
    # Test element not in array
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 6) == (-1, -1)
    
    # Test empty array
    assert find_first_last_occurrence([], 5) == (-1, -1)
    
    # Test array with only one element
    assert find_first_last_occurrence([5], 5) == (0, 0)
    
    # Test array with one occurrence at the start
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 1) == (0, 0)
    
    # Test array with one occurrence at the end
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 5) == (4, 4)
    
    # Test array with multiple occurrences at the start
    assert find_first_last_occurrence([2, 2, 2, 3, 4, 5], 2) == (0, 2)
    
    # Test array with multiple occurrences at the end
    assert find_first_last_occurrence([1, 2, 3, 4, 5, 5, 5], 5) == (4, 6)

def test_find_first_last_occurrence_error_handling():
    # Additional error handling tests
    with pytest.raises(TypeError):
        find_first_last_occurrence(None, 5)
    
    with pytest.raises(TypeError):
        find_first_last_occurrence([1, 2, 3], None)