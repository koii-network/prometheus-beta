import pytest
from src.find_pairs import find_pairs_sum_to_target

def test_find_pairs_sum_to_target():
    # Test basic scenario
    assert sorted(find_pairs_sum_to_target([1, 2, 3, 4, 5], 6)) == [(1, 5), (2, 4)]
    
    # Test with duplicate numbers
    assert sorted(find_pairs_sum_to_target([1, 1, 2, 3, 4, 4, 5], 6)) == [(1, 5), (2, 4)]
    
    # Test with no pairs
    assert find_pairs_sum_to_target([1, 2, 3, 4], 10) == []
    
    # Test with empty list
    assert find_pairs_sum_to_target([], 5) == []
    
    # Test with negative numbers
    assert sorted(find_pairs_sum_to_target([-1, 0, 1, 2, -2, 3], 1)) == [(-2, 3), (0, 1)]
    
    # Test with zero target
    assert sorted(find_pairs_sum_to_target([-1, 0, 1, 2, -2], 0)) == [(-2, 2), (-1, 1)]

def test_find_pairs_error_handling():
    # Verify function works with different input types
    with pytest.raises(TypeError):
        find_pairs_sum_to_target(None, 5)
    
    with pytest.raises(TypeError):
        find_pairs_sum_to_target([1, 2, 3], None)