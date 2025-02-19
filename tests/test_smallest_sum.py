import pytest
from src.smallest_sum import find_smallest_possible_sum

def test_find_smallest_possible_sum_normal_case():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected = 1 + 2 + 3  # min(1,4) + min(2,5) + min(3,6)
    assert find_smallest_possible_sum(list1, list2) == 6

def test_find_smallest_possible_sum_mixed_case():
    list1 = [3, 1, 2]
    list2 = [6, 4, 5]
    expected = 1 + 2 + 3
    assert find_smallest_possible_sum(list1, list2) == 6

def test_find_smallest_possible_sum_same_lists():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    expected = 1 + 2 + 3
    assert find_smallest_possible_sum(list1, list2) == 6

def test_find_smallest_possible_sum_empty_lists():
    list1 = []
    list2 = []
    expected = 0
    assert find_smallest_possible_sum(list1, list2) == 0

def test_find_smallest_possible_sum_different_length_raises_error():
    list1 = [1, 2, 3]
    list2 = [4, 5]
    with pytest.raises(ValueError, match="Input lists must have the same length"):
        find_smallest_possible_sum(list1, list2)