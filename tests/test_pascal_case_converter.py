import pytest
from src.pascal_case_converter import to_pascal_case

def test_basic_pascal_case_conversion():
    assert to_pascal_case("hello world") == "HelloWorld"
    assert to_pascal_case("hello_world") == "HelloWorld"
    assert to_pascal_case("hello-world") == "HelloWorld"

def test_pascal_case_with_mixed_separators():
    assert to_pascal_case("hello_world-test") == "HelloWorldTest"
    assert to_pascal_case("hello__world--test") == "HelloWorldTest"

def test_pascal_case_with_numbers():
    assert to_pascal_case("hello2world") == "Hello2World"
    assert to_pascal_case("hello_2_world") == "Hello2World"

def test_pascal_case_empty_string():
    assert to_pascal_case("") == ""

def test_pascal_case_single_word():
    assert to_pascal_case("hello") == "Hello"

def test_pascal_case_error_handling():
    with pytest.raises(TypeError):
        to_pascal_case(123)
    with pytest.raises(TypeError):
        to_pascal_case(None)