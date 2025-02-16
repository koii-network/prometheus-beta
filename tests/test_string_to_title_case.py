import pytest
from src.string_to_title_case import convert_to_title_case

def test_basic_title_case():
    """Test basic title case conversion."""
    assert convert_to_title_case("hello world") == "Hello World"

def test_already_title_case():
    """Test a string that is already in title case."""
    assert convert_to_title_case("Hello World") == "Hello World"

def test_mixed_case():
    """Test a string with mixed case."""
    assert convert_to_title_case("hElLo wOrLd") == "Hello World"

def test_empty_string():
    """Test an empty string."""
    assert convert_to_title_case("") == ""

def test_single_word():
    """Test a single word."""
    assert convert_to_title_case("python") == "Python"

def test_string_with_numbers():
    """Test a string with numbers."""
    assert convert_to_title_case("hello 123 world") == "Hello 123 World"

def test_string_with_special_chars():
    """Test a string with special characters."""
    assert convert_to_title_case("hello, world!") == "Hello, World!"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_title_case(123)
        convert_to_title_case(None)