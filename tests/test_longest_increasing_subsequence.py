import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_case():
    assert find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == [10, 22, 33, 50, 60, 80]

def test_already_sorted():
    assert find_longest_increasing_subsequence([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    assert find_longest_increasing_subsequence([5, 4, 3, 2, 1]) == [5]

def test_empty_list():
    assert find_longest_increasing_subsequence([]) == []

def test_single_element():
    assert find_longest_increasing_subsequence([42]) == [42]

def test_multiple_same_length_subsequences():
    # Different valid subsequences are possible
    result = find_longest_increasing_subsequence([1, 3, 6, 7, 9, 4, 10, 5, 6])
    assert result == [1, 3, 6, 7, 9, 10]

def test_non_list_input():
    with pytest.raises(TypeError):
        find_longest_increasing_subsequence("not a list")

def test_non_numeric_input():
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2, "three", 4])

def test_mixed_type_input():
    with pytest.raises(ValueError):
        find_longest_increasing_subsequence([1, 2.5, 3, 4])