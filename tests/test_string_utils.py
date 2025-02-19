import pytest
from src.string_utils import to_camel_case

def test_to_camel_case_basic():
    assert to_camel_case("hello world") == "helloWorld"
    assert to_camel_case("hello-world") == "helloWorld"
    assert to_camel_case("hello_world") == "helloWorld"

def test_to_camel_case_multiple_words():
    assert to_camel_case("convert to camel case") == "convertToCamelCase"
    assert to_camel_case("convert-to-camel-case") == "convertToCamelCase"
    assert to_camel_case("convert_to_camel_case") == "convertToCamelCase"

def test_to_camel_case_edge_cases():
    assert to_camel_case("") == ""
    assert to_camel_case("x") == "x"
    assert to_camel_case("X") == "x"

def test_to_camel_case_error_handling():
    with pytest.raises(TypeError):
        to_camel_case(None)
    with pytest.raises(TypeError):
        to_camel_case(123)

def test_to_camel_case_mixed_separators():
    assert to_camel_case("hello world-test_case") == "helloWorldTestCase"