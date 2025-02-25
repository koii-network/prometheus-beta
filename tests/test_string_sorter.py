import pytest
from src.string_sorter import sort_strings_by_length

def test_sort_strings_by_length_normal_case():
    """Test sorting a list of strings by length"""
    input_list = ["apple", "pear", "banana", "kiwi"]
    expected = ["kiwi", "pear", "apple", "banana"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_empty_list():
    """Test sorting an empty list"""
    assert sort_strings_by_length([]) == []

def test_sort_strings_by_length_same_length():
    """Test sorting strings of the same length"""
    input_list = ["cat", "dog", "rat"]
    expected = ["cat", "dog", "rat"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_mixed_lengths():
    """Test sorting a list with mixed string lengths"""
    input_list = ["a", "hello", "world", "hi", "python"]
    expected = ["a", "hi", "hello", "world", "python"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_strings_by_length("not a list")

def test_sort_strings_by_length_invalid_element_type():
    """Test raising TypeError for list with non-string elements"""
    with pytest.raises(TypeError, match="All elements must be strings"):
        sort_strings_by_length([1, "string", 3.14])