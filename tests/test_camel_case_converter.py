import pytest
from src.camel_case_converter import to_camel_case

def test_to_camel_case_with_spaces():
    assert to_camel_case("hello world") == "helloWorld"
    assert to_camel_case("hello world python") == "helloWorldPython"

def test_to_camel_case_with_hyphens():
    assert to_camel_case("hello-world") == "helloWorld"
    assert to_camel_case("hello-world-python") == "helloWorldPython"

def test_to_camel_case_with_underscores():
    assert to_camel_case("hello_world") == "helloWorld"
    assert to_camel_case("hello_world_python") == "helloWorldPython"

def test_to_camel_case_mixed_separators():
    assert to_camel_case("hello-world_python") == "helloWorldPython"

def test_to_camel_case_empty_string():
    assert to_camel_case("") == ""

def test_to_camel_case_single_word():
    assert to_camel_case("hello") == "hello"
    assert to_camel_case("World") == "world"