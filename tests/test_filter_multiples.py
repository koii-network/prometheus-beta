import pytest
from src.filter_multiples import filter_special_multiples

def test_filter_special_multiples():
    # Test normal case with mixed numbers
    assert filter_special_multiples([1, 2, 3, 5, 6, 9, 10, 15]) == [3, 5, 6, 10]
    
    # Test empty list
    assert filter_special_multiples([]) == []
    
    # Test list with no special multiples
    assert filter_special_multiples([1, 2, 4, 7, 8]) == []
    
    # Test list with only 3 or 5 multiples
    assert filter_special_multiples([3, 6, 9, 12]) == [3, 6, 9, 12]
    assert filter_special_multiples([5, 10, 20]) == [5, 10, 20]
    
    # Test with negative numbers
    assert filter_special_multiples([-3, -5, -6, -10, -15]) == [-6, -5, -3, -10]
    
    # Test with larger list of numbers
    numbers = list(range(1, 21))
    assert filter_special_multiples(numbers) == [3, 5, 6, 9, 10, 12, 15, 18, 20]

def test_filter_special_multiples_sorting():
    # Ensure the output is always sorted
    unsorted_input = [10, 3, 15, 5, 6, 9]
    assert filter_special_multiples(unsorted_input) == [3, 5, 6, 9, 10]