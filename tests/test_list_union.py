import pytest
from src.list_union import find_list_union

def test_basic_union():
    """Test union of two lists with no duplicates."""
    result = find_list_union([1, 2, 3], [4, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]

def test_union_with_duplicates():
    """Test union of lists with duplicates."""
    result = find_list_union([1, 2, 3, 2], [3, 4, 5, 3])
    assert result == [1, 2, 3, 4, 5]

def test_union_order_preservation():
    """Test that the order of first occurrence is preserved."""
    result = find_list_union([3, 1, 2], [2, 4, 3])
    assert result == [3, 1, 2, 4]

def test_empty_lists():
    """Test union with empty lists."""
    assert find_list_union([], []) == []
    assert find_list_union([1, 2], []) == [1, 2]
    assert find_list_union([], [3, 4]) == [3, 4]

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        find_list_union(1, [2, 3])
    with pytest.raises(TypeError):
        find_list_union([1, 2], "not a list")
    with pytest.raises(TypeError):
        find_list_union(None, [])

def test_mixed_type_lists():
    """Test union of lists with mixed types."""
    result = find_list_union([1, 'a', 2], ['b', 2, 3])
    assert result == [1, 'a', 2, 'b', 3]