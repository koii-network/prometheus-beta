import pytest
from src.unique_pairs import find_unique_pairs

def test_basic_unique_pairs():
    """Test finding unique pairs in a simple list"""
    result = find_unique_pairs([1, 2, 3])
    assert set(result) == {(1, 2), (1, 3), (2, 3)}
    assert len(result) == 3

def test_empty_list():
    """Test behavior with an empty list"""
    assert find_unique_pairs([]) == []

def test_single_element_list():
    """Test behavior with a single-element list"""
    assert find_unique_pairs([1]) == []

def test_list_with_duplicates():
    """Test that duplicates are handled correctly"""
    result = find_unique_pairs([1, 1, 2, 2, 3])
    assert set(result) == {(1, 2), (1, 3), (2, 3)}
    assert len(result) == 3

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_unique_pairs("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_unique_pairs(123)

def test_large_list():
    """Test with a larger list of numbers"""
    input_list = [1, 2, 3, 4, 5]
    expected_pairs = [(1, 2), (1, 3), (1, 4), (1, 5), 
                      (2, 3), (2, 4), (2, 5), 
                      (3, 4), (3, 5), 
                      (4, 5)]
    result = find_unique_pairs(input_list)
    assert set(result) == set(expected_pairs)
    assert len(result) == 10