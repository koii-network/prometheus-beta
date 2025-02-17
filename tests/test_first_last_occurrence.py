import pytest
from src.first_last_occurrence import find_first_last_occurrence

def test_find_first_last_occurrence():
    # Normal case with multiple occurrences
    assert find_first_last_occurrence([1, 2, 2, 2, 3, 4, 5], 2) == (1, 3)
    
    # Case with single occurrence
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 3) == (2, 2)
    
    # Case with element at the beginning
    assert find_first_last_occurrence([1, 1, 1, 2, 3, 4], 1) == (0, 2)
    
    # Case with element at the end
    assert find_first_last_occurrence([1, 2, 3, 4, 5, 5, 5], 5) == (4, 6)
    
    # Case with element not in array
    assert find_first_last_occurrence([1, 2, 3, 4, 5], 6) == (-1, -1)
    
    # Empty array case
    assert find_first_last_occurrence([], 1) == (-1, -1)

def test_error_handling():
    # Test with non-sortable array
    with pytest.raises(TypeError):
        find_first_last_occurrence(['a', 'b', 'c'], 'b')
    
    # Test with None input
    with pytest.raises(TypeError):
        find_first_last_occurrence(None, 1)