import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 1, 4, 2]) == 4

def test_find_second_largest_with_duplicates():
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 4, 4, 3, 3]) == 4

def test_find_second_largest_negative_numbers():
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([0, -1, -2, 1, 2]) == 0

def test_find_second_largest_edge_cases():
    with pytest.raises(ValueError):
        find_second_largest([1])
    
    with pytest.raises(ValueError):
        find_second_largest([])
    
    with pytest.raises(ValueError):
        find_second_largest([1, 1, 1])

def test_find_second_largest_floating_point():
    assert find_second_largest([1.5, 2.7, 0.3, 4.1]) == 2.7