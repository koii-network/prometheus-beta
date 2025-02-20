import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_increasing_sequence():
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_mixed_sequence():
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_empty_list():
    assert longest_increasing_subsequence([]) == 0

def test_single_element():
    assert longest_increasing_subsequence([42]) == 1

def test_all_decreasing_sequence():
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_duplicate_elements():
    assert longest_increasing_subsequence([1, 2, 2, 3, 1, 4]) == 4

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")

def test_non_integer_elements():
    with pytest.raises(ValueError):
        longest_increasing_subsequence([1, 2, "3", 4])

def test_negative_numbers():
    assert longest_increasing_subsequence([-1, -2, 0, 1, 2]) == 4