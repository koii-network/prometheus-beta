import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 5, 4, 3, 2, 1]) == 4
    assert find_second_largest([10, 5, 8, 3, 6]) == 8

def test_find_second_largest_with_duplicates():
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2

def test_find_second_largest_error_cases():
    # Empty array
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_second_largest([])
    
    # Array with only one unique element
    with pytest.raises(ValueError, match="Array must contain at least two unique elements"):
        find_second_largest([5, 5, 5, 5])

def test_find_second_largest_negative_numbers():
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([0, -1, -2, 5, 3]) == 3