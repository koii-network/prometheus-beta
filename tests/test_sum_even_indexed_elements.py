import pytest
from src.sum_even_indexed_elements import sum_even_indexed_elements

def test_sum_even_indexed_elements_basic():
    """Test sum of even-indexed elements in a standard list."""
    assert sum_even_indexed_elements([1, 2, 3, 4, 5]) == 9

def test_sum_even_indexed_elements_negative():
    """Test sum of even-indexed elements with negative numbers."""
    assert sum_even_indexed_elements([-1, 10, 20, 30, 40]) == 59

def test_sum_even_indexed_elements_empty():
    """Test sum of even-indexed elements in an empty list."""
    assert sum_even_indexed_elements([]) == 0

def test_sum_even_indexed_elements_single_element():
    """Test sum of even-indexed elements with a single element."""
    assert sum_even_indexed_elements([42]) == 42

def test_sum_even_indexed_elements_alternating():
    """Test sum of even-indexed elements with mixed positive and negative numbers."""
    assert sum_even_indexed_elements([1, -2, 3, -4, 5]) == 9

def test_sum_even_indexed_elements_type_error():
    """Test that a type error is raised for non-list input."""
    with pytest.raises(TypeError):
        sum_even_indexed_elements("not a list")