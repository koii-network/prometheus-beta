import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_with_duplicates():
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 4, 4, 3, 3]) == 4

def test_find_second_largest_edge_cases():
    assert find_second_largest([1, 1, 2]) == 1
    assert find_second_largest([2, 1]) == 1

def test_find_second_largest_error_cases():
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_second_largest([])
    
    with pytest.raises(ValueError, match="Array must have at least two distinct numbers"):
        find_second_largest([1, 1, 1])
        
def test_find_second_largest_negative_numbers():
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([-5, 0, 5]) == 0