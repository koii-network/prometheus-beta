import pytest
from src.string_utils import capitalize_strings

def test_capitalize_strings_basic():
    """Test basic string capitalization"""
    input_list = ["hello", "world", "python"]
    expected = ["Hello", "World", "Python"]
    assert capitalize_strings(input_list) == expected

def test_capitalize_strings_already_capitalized():
    """Test list with already capitalized strings"""
    input_list = ["Hello", "World"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_list) == expected

def test_capitalize_strings_mixed_case():
    """Test list with mixed case strings"""
    input_list = ["hElLo", "wOrLd"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_list) == expected

def test_capitalize_strings_empty_list():
    """Test with an empty list"""
    assert capitalize_strings([]) == []

def test_capitalize_strings_invalid_input_not_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        capitalize_strings("not a list")

def test_capitalize_strings_invalid_input_non_string_elements():
    """Test raising ValueError for list with non-string elements"""
    with pytest.raises(ValueError, match="All elements must be strings"):
        capitalize_strings(["valid", 123, "string"])