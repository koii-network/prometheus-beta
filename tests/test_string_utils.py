import pytest
from src.string_utils import capitalize_strings

def test_capitalize_strings_normal_case():
    """Test capitalizing a list of strings."""
    input_list = ["hello", "world", "python"]
    expected = ["Hello", "World", "Python"]
    assert capitalize_strings(input_list) == expected

def test_capitalize_strings_empty_list():
    """Test with an empty list."""
    assert capitalize_strings([]) == []

def test_capitalize_strings_already_capitalized():
    """Test with already capitalized strings."""
    input_list = ["Hello", "World"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_list) == expected

def test_capitalize_strings_mixed_case():
    """Test with mixed case strings."""
    input_list = ["hELLO", "wORLD"]
    expected = ["Hello", "World"]
    assert capitalize_strings(input_list) == expected

def test_capitalize_strings_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        capitalize_strings("not a list")

def test_capitalize_strings_non_string_elements():
    """Test that TypeError is raised for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        capitalize_strings(["hello", 42, True])

def test_capitalize_strings_single_char_strings():
    """Test with single character strings."""
    input_list = ["a", "b", "c"]
    expected = ["A", "B", "C"]
    assert capitalize_strings(input_list) == expected