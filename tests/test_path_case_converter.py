import pytest
from src.path_case_converter import convert_to_path_case

def test_convert_to_path_case_basic():
    assert convert_to_path_case("hello world") == "hello/world"
    assert convert_to_path_case("hello_world") == "hello/world"
    assert convert_to_path_case("helloWorld") == "hello/world"

def test_convert_to_path_case_complex():
    assert convert_to_path_case("HelloWorld") == "hello/world"
    assert convert_to_path_case("hello world_test") == "hello/world/test"
    assert convert_to_path_case("camelCaseTest") == "camel/case/test"

def test_convert_to_path_case_edge_cases():
    assert convert_to_path_case("") == ""
    assert convert_to_path_case("SingleWord") == "single/word"
    assert convert_to_path_case("multiple///slashes") == "multiple/slashes"

def test_convert_to_path_case_error_handling():
    with pytest.raises(TypeError):
        convert_to_path_case(123)
    with pytest.raises(TypeError):
        convert_to_path_case(None)