import pytest
from src.string_sorter import sort_strings_by_length

def test_sort_strings_by_length_ascending():
    # Test ascending order (default)
    input_list = ["a", "ccc", "bb"]
    expected = ["a", "bb", "ccc"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_descending():
    # Test descending order
    input_list = ["a", "ccc", "bb"]
    expected = ["ccc", "bb", "a"]
    assert sort_strings_by_length(input_list, reverse=True) == expected

def test_empty_list():
    # Test empty list
    assert sort_strings_by_length([]) == []

def test_single_element_list():
    # Test list with single element
    assert sort_strings_by_length(["hello"]) == ["hello"]

def test_equal_length_strings():
    # Test strings of equal length
    input_list = ["cat", "dog", "bat"]
    assert sort_strings_by_length(input_list) == ["cat", "dog", "bat"]

def test_invalid_input_type():
    # Test invalid input type
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_strings_by_length("not a list")

def test_non_string_elements():
    # Test list with non-string elements
    with pytest.raises(TypeError, match="All elements must be strings"):
        sort_strings_by_length(["a", 1, "b"])