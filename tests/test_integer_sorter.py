import pytest
from src.integer_sorter import sort_integers

def test_sort_normal_list():
    """Test sorting a list of positive and negative integers."""
    input_list = [5, 2, -3, 0, 1]
    expected = [-3, 0, 1, 2, 5]
    assert sort_integers(input_list) == expected

def test_already_sorted_list():
    """Test list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert sort_integers(input_list) == input_list

def test_reverse_sorted_list():
    """Test list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert sort_integers(input_list) == expected

def test_list_with_duplicates():
    """Test list with duplicate values."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert sort_integers(input_list) == expected

def test_empty_list():
    """Test sorting an empty list."""
    assert sort_integers([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert sort_integers([42]) == [42]

def test_invalid_input_not_list():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_integers("not a list")

def test_invalid_input_non_integers():
    """Test that list with non-integer elements raises TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sort_integers([1, 2, "3", 4])

def test_large_list():
    """Test sorting a large list of integers."""
    import random
    random.seed(42)  # For reproducibility
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]
    assert sort_integers(large_list) == sorted(large_list)