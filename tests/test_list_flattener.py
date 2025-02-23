import pytest
from src.list_flattener import flatten_nested_list

def test_flatten_simple_list():
    """Test flattening a non-nested list."""
    assert flatten_nested_list([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list."""
    assert flatten_nested_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_nested_list([]) == []

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    nested = [1, [2, [3, [4]]], 5, [6, 7]]
    assert flatten_nested_list(nested) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types of nested elements."""
    nested = [1, 'a', [2, 'b', [3, 'c']], 4]
    assert flatten_nested_list(nested) == [1, 'a', 2, 'b', 3, 'c', 4]

def test_flatten_single_element_list():
    """Test flattening a list with a single nested element."""
    assert flatten_nested_list([1]) == [1]
    assert flatten_nested_list([[1]]) == [1]

def test_flatten_non_list_input():
    """Test flattening a non-list input."""
    assert flatten_nested_list(5) == [5]
    assert flatten_nested_list('string') == ['string']

def test_nested_empty_lists():
    """Test flattening list with nested empty lists."""
    assert flatten_nested_list([[], [1, []], 2]) == [1, 2]