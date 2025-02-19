import pytest
from src.longest_increasing_subsequence import find_lis_length

def test_find_lis_length_normal_case():
    assert find_lis_length([10, 22, 9, 33, 21, 50, 41, 60]) == 5

def test_find_lis_length_sorted_ascending():
    assert find_lis_length([1, 2, 3, 4, 5]) == 5

def test_find_lis_length_sorted_descending():
    assert find_lis_length([5, 4, 3, 2, 1]) == 1

def test_find_lis_length_empty_list():
    assert find_lis_length([]) == 0

def test_find_lis_length_single_element():
    assert find_lis_length([42]) == 1

def test_find_lis_length_duplicate_elements():
    assert find_lis_length([7, 7, 7, 7]) == 1

def test_find_lis_length_mixed_elements():
    assert find_lis_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_find_lis_length_invalid_input_type():
    with pytest.raises(TypeError):
        find_lis_length("not a list")

def test_find_lis_length_invalid_list_content():
    with pytest.raises(ValueError):
        find_lis_length([1, 2, "three", 4])