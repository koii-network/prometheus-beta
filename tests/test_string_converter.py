import pytest
from src.string_converter import convert_to_header_case

def test_convert_to_header_case_basic():
    """Test basic string conversion to header case."""
    assert convert_to_header_case("hello world") == "HelloWorld"
    assert convert_to_header_case("hello_world") == "HelloWorld"
    assert convert_to_header_case("hello-world") == "HelloWorld"

def test_convert_to_header_case_multiple_words():
    """Test conversion of strings with multiple words and different separators."""
    assert convert_to_header_case("hello world_test-case") == "HelloWorldTestCase"
    assert convert_to_header_case("python_is_awesome") == "PythonIsAwesome"
    assert convert_to_header_case("convert-to-header-case") == "ConvertToHeaderCase"

def test_convert_to_header_case_edge_cases():
    """Test edge cases for header case conversion."""
    assert convert_to_header_case("") == ""
    assert convert_to_header_case(None) == ""
    assert convert_to_header_case("a") == "A"
    assert convert_to_header_case("A") == "A"

def test_convert_to_header_case_mixed_separators():
    """Test conversion with mixed separators."""
    assert convert_to_header_case("hello_world-test case") == "HelloWorldTestCase"