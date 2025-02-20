import pytest
from src.remove_duplicates import remove_duplicates_and_sort

def test_remove_duplicates_and_sort():
    # Test case with duplicates
    assert remove_duplicates_and_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 2, 3, 4, 5, 6, 9]
    
    # Test case with no duplicates
    assert remove_duplicates_and_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case with empty list
    assert remove_duplicates_and_sort([]) == []
    
    # Test case with all duplicate elements
    assert remove_duplicates_and_sort([7, 7, 7, 7]) == [7]
    
    # Test case with negative numbers
    assert remove_duplicates_and_sort([-3, -1, -3, 0, 2, -1, 5]) == [-3, -1, 0, 2, 5]

def test_input_types():
    # Test with input that is not a list
    with pytest.raises(TypeError):
        remove_duplicates_and_sort("not a list")
    
    with pytest.raises(TypeError):
        remove_duplicates_and_sort(123)

def test_edge_cases():
    # Test with a single element
    assert remove_duplicates_and_sort([42]) == [42]
    
    # Test with large numbers of duplicates
    large_dup_list = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]
    assert remove_duplicates_and_sort(large_dup_list) == [1, 2, 3, 4, 5]