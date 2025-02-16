import pytest
from src.radix_sort import radix_sort

def test_radix_sort_normal_case():
    """Test radix sort with a standard list of non-negative integers."""
    input_list = [170, 45, 75, 90, 802, 24, 2, 66]
    expected = [2, 24, 45, 66, 75, 90, 170, 802]
    assert radix_sort(input_list) == expected

def test_radix_sort_empty_list():
    """Test radix sort with an empty list."""
    assert radix_sort([]) == []

def test_radix_sort_single_element():
    """Test radix sort with a single element."""
    assert radix_sort([42]) == [42]

def test_radix_sort_already_sorted():
    """Test radix sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert radix_sort(input_list) == input_list

def test_radix_sort_reverse_sorted():
    """Test radix sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert radix_sort(input_list) == expected

def test_radix_sort_with_duplicates():
    """Test radix sort with duplicate values."""
    input_list = [5, 2, 9, 1, 5, 6, 2]
    expected = [1, 2, 2, 5, 5, 6, 9]
    assert radix_sort(input_list) == expected

def test_radix_sort_negative_input_raises_error():
    """Test that radix sort raises an error for negative numbers."""
    with pytest.raises(ValueError, match="Radix sort only works with non-negative integers"):
        radix_sort([-1, 2, 3])

def test_radix_sort_non_integer_input_raises_error():
    """Test that radix sort raises an error for non-integer inputs."""
    with pytest.raises(ValueError, match="Radix sort only works with non-negative integers"):
        radix_sort([1, 2, 'a'])