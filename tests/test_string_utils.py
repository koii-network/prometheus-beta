import pytest
from src.string_utils import capitalize_strings

def test_capitalize_strings_normal_case():
    """Test capitalization of normal string array"""
    input_array = ["hello", "world", "python"]
    expected = ["Hello", "World", "Python"]
    assert capitalize_strings(input_array) == expected

def test_capitalize_strings_empty_list():
    """Test with an empty list"""
    assert capitalize_strings([]) == []

def test_capitalize_strings_already_capitalized():
    """Test with already capitalized strings"""
    input_array = ["Hello", "World"]
    assert capitalize_strings(input_array) == ["Hello", "World"]

def test_capitalize_strings_mixed_case():
    """Test with mixed case strings"""
    input_array = ["hElLo", "wORlD"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_array) == expected

def test_capitalize_strings_invalid_input_type():
    """Test with invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        capitalize_strings("not a list")

def test_capitalize_strings_non_string_elements():
    """Test with non-string elements in the list"""
    with pytest.raises(TypeError, match="All elements in the list must be strings"):
        capitalize_strings(["hello", 42, "world"])