import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test bitonic sort with ascending order"""
    test_cases = [
        [5, 2, 9, 1, 7, 6, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        []
    ]
    
    for case in test_cases:
        result = bitonic_sort(case)
        assert result == sorted(case), f"Failed on input {case}"

def test_bitonic_sort_descending():
    """Test bitonic sort with descending order"""
    test_cases = [
        [5, 2, 9, 1, 7, 6, 3],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1]
    ]
    
    for case in test_cases:
        result = bitonic_sort(case, ascending=False)
        assert result == sorted(case, reverse=True), f"Failed on input {case}"

def test_bitonic_sort_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")
    
    with pytest.raises(TypeError):
        bitonic_sort(None)

def test_bitonic_sort_edge_cases():
    """Test edge cases"""
    # Lists with repeated elements
    test_cases = [
        [1, 1, 1, 1],
        [3, 3, 2, 2, 1, 1],
        [1, 2, 2, 1, 3, 3]
    ]
    
    for case in test_cases:
        result = bitonic_sort(case)
        assert result == sorted(case), f"Failed on input {case}"