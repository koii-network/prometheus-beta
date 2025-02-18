import pytest
from src.strand_sort import strand_sort, merge

def test_strand_sort_empty_list():
    """Test sorting an empty list."""
    assert strand_sort([]) == []

def test_strand_sort_single_element():
    """Test sorting a list with a single element."""
    assert strand_sort([5]) == [5]

def test_strand_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert strand_sort(input_list) == input_list

def test_strand_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert strand_sort(input_list) == [1, 2, 3, 4, 5]

def test_strand_sort_random_list():
    """Test sorting a random list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert strand_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_strand_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert strand_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_merge_function():
    """Test the merge helper function."""
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]
    assert merge(list1, list2) == [1, 2, 3, 4, 5, 6]

def test_merge_with_unequal_lengths():
    """Test merging lists of different lengths."""
    list1 = [1, 3, 5, 7]
    list2 = [2, 4]
    assert merge(list1, list2) == [1, 2, 3, 4, 5, 7]

def test_merge_one_empty_list():
    """Test merging with an empty list."""
    list1 = [1, 2, 3]
    list2 = []
    assert merge(list1, list2) == [1, 2, 3]