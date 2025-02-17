import pytest
from src.find_second_largest import find_second_largest

def test_normal_case():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 5, 4, 3, 2, 1]) == 4

def test_duplicate_numbers():
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2

def test_single_unique_number():
    assert find_second_largest([1, 1, 1]) is None

def test_negative_numbers():
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_mixed_numbers():
    assert find_second_largest([-10, 0, 10, 5]) == 5

def test_empty_input():
    with pytest.raises(ValueError):
        find_second_largest([])

def test_none_input():
    with pytest.raises(ValueError):
        find_second_largest(None)

def test_non_numeric_input():
    with pytest.raises(TypeError):
        find_second_largest([1, 2, '3'])
        
def test_float_numbers():
    assert find_second_largest([1.5, 2.5, 3.5]) == 2.5