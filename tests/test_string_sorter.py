import pytest
from src.string_sorter import sort_strings_by_length

def test_sort_strings_ascending():
    input_list = ["apple", "banana", "cherry", "date"]
    expected = ["date", "apple", "banana", "cherry"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_descending():
    input_list = ["apple", "banana", "cherry", "date"]
    expected = ["banana", "cherry", "apple", "date"]
    assert sort_strings_by_length(input_list, reverse=True) == expected

def test_empty_list():
    assert sort_strings_by_length([]) == []

def test_single_element_list():
    assert sort_strings_by_length(["hello"]) == ["hello"]

def test_equal_length_strings():
    input_list = ["cat", "dog", "rat", "bat"]
    # When strings have equal length, original order is maintained
    assert sort_strings_by_length(input_list) == input_list

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_strings_by_length("not a list")

def test_invalid_element_type():
    with pytest.raises(TypeError, match="All elements must be strings"):
        sort_strings_by_length(["valid", 123, "invalid"])