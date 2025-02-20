import pytest
from src.most_frequent_index import get_most_frequent_index

def test_basic_most_frequent():
    # Simple case with one clear most frequent number
    assert get_most_frequent_index([1, 2, 2, 3, 3, 3]) == 3

def test_first_occurrence_in_tie():
    # When multiple numbers have the same frequency, return first occurrence
    assert get_most_frequent_index([1, 2, 1, 2, 3, 3]) == 0

def test_single_element_list():
    # List with a single element
    assert get_most_frequent_index([5]) == 0

def test_all_unique_elements():
    # When all elements appear once, return first index
    assert get_most_frequent_index([5, 4, 3, 2, 1]) == 0

def test_multiple_max_frequency():
    # Multiple numbers with same max frequency
    assert get_most_frequent_index([1, 2, 1, 2, 3]) == 0

def test_empty_list_raises_error():
    # Empty list should raise ValueError
    with pytest.raises(ValueError):
        get_most_frequent_index([])