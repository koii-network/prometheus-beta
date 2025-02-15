import pytest
from src.count_occurrences import count_occurrences

def test_count_occurrences_basic():
    # Test counting occurrences of a number
    assert count_occurrences([1, 2, 3, 2, 2, 4], 2) == 3
    assert count_occurrences([1, 2, 3, 2, 2, 4], 5) == 0

def test_count_occurrences_strings():
    # Test counting occurrences of strings
    assert count_occurrences(["apple", "banana", "apple", "cherry"], "apple") == 2
    assert count_occurrences(["apple", "banana", "apple", "cherry"], "grape") == 0

def test_count_occurrences_mixed_types():
    # Test counting occurrences in mixed type array
    assert count_occurrences([1, "1", 1, "1", 2], 1) == 2
    assert count_occurrences([1, "1", 1, "1", 2], "1") == 2

def test_count_occurrences_empty_list():
    # Test with an empty list
    assert count_occurrences([], 5) == 0

def test_count_occurrences_invalid_input():
    # Test invalid input types
    with pytest.raises(TypeError):
        count_occurrences(None, 5)
    with pytest.raises(TypeError):
        count_occurrences("not a list", 5)
    with pytest.raises(TypeError):
        count_occurrences(123, 5)