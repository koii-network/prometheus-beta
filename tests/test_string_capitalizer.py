import pytest
from src.string_capitalizer import capitalize_strings

def test_basic_capitalization():
    """Test basic string capitalization."""
    input_array = ["hello", "world"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_array) == expected

def test_empty_array():
    """Test capitalization of an empty array."""
    assert capitalize_strings([]) == []

def test_already_capitalized():
    """Test array with already capitalized strings."""
    input_array = ["Hello", "World"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_array) == expected

def test_mixed_case():
    """Test array with mixed case strings."""
    input_array = ["hElLo", "wOrLd"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_array) == expected

def test_single_character_strings():
    """Test array with single character strings."""
    input_array = ["a", "b", "c"]
    expected = ["A", "B", "C"]
    assert capitalize_strings(input_array) == expected

def test_invalid_input_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        capitalize_strings("not a list")

def test_invalid_input_non_string_elements():
    """Test that a TypeError is raised for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        capitalize_strings(["hello", 123, "world"])

def test_whitespace_strings():
    """Test capitalization of strings with leading/trailing whitespace."""
    input_array = [" hello", "world "]
    expected = ["Hello", "World "]
    assert capitalize_strings(input_array) == expected