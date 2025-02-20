import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_sequence():
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6

def test_already_sorted_sequence():
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_reverse_sorted_sequence():
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_empty_list():
    assert longest_increasing_subsequence([]) == 0

def test_single_element_list():
    assert longest_increasing_subsequence([42]) == 1

def test_duplicate_elements():
    assert longest_increasing_subsequence([1, 1, 1, 1]) == 1

def test_complex_sequence():
    assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_negative_numbers():
    assert longest_increasing_subsequence([-7, -1, 5, 2, 3, 9, -3]) == 4

def test_input_type_error():
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")

def test_input_value_error():
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, "3", 4])