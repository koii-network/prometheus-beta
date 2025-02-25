"""
Tests for the path case conversion function.
"""

import pytest
from src.path_case_converter import to_path_case


def test_basic_string_conversion():
    """Test basic string to path case conversion."""
    assert to_path_case("Hello World") == "hello-world"
    assert to_path_case("snake_case_string") == "snake-case-string"
    assert to_path_case("camelCaseString") == "camel-case-string"


def test_mixed_separators():
    """Test conversion with mixed separators."""
    assert to_path_case("  Mixed  Separators  ") == "mixed-separators"
    assert to_path_case("mixed_and camelCase Separators") == "mixed-and-camel-case-separators"


def test_empty_and_whitespace_strings():
    """Test empty and whitespace-only strings."""
    assert to_path_case("") == ""
    assert to_path_case("   ") == ""


def test_already_path_case():
    """Test strings that are already in path case."""
    assert to_path_case("already-in-path-case") == "already-in-path-case"


def test_numeric_strings():
    """Test strings with numbers."""
    assert to_path_case("hello123World") == "hello123-world"
    assert to_path_case("123HelloWorld") == "123-hello-world"


def test_special_case_conversions():
    """Test various special case conversions."""
    assert to_path_case("XML_HTTPRequest") == "xml-http-request"
    assert to_path_case("iOS_App") == "i-os-app"


def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_path_case(None)
    
    with pytest.raises(TypeError):
        to_path_case(123)
    
    with pytest.raises(TypeError):
        to_path_case(["list"])