import pytest
from src.delete_duplicates import deleteDuplicates

def test_delete_duplicates():
    # Test case with duplicates
    assert deleteDuplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]
    
    # Test case with no duplicates
    assert deleteDuplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case with all duplicates
    assert deleteDuplicates([1, 1, 1, 1]) == [1]
    
    # Test case with empty array
    assert deleteDuplicates([]) == []
    
    # Test case with mixed type duplicates (if using more flexible list)
    assert deleteDuplicates([1, 'a', 1, 'b', 'a', 2]) == [1, 'a', 'b', 2]

def test_order_preservation():
    # Ensure original order is maintained
    original = [5, 2, 1, 5, 4, 2, 3, 1]
    expected = [5, 2, 1, 4, 3]
    assert deleteDuplicates(original) == expected