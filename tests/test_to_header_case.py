import pytest
from src.to_header_case import to_header_case

def test_to_header_case_basic():
    assert to_header_case("hello world") == "HelloWorld"
    assert to_header_case("hello_world") == "HelloWorld"
    assert to_header_case("hello-world") == "HelloWorld"

def test_to_header_case_mixed_separators():
    assert to_header_case("hello_world-test") == "HelloWorldTest"
    assert to_header_case("hello world_test-case") == "HelloWorldTestCase"

def test_to_header_case_edge_cases():
    assert to_header_case("") == ""
    assert to_header_case("a") == "A"
    assert to_header_case("a b c") == "ABC"

def test_to_header_case_already_capitalized():
    assert to_header_case("HelloWorld") == "HelloWorld"
    assert to_header_case("Hello_World") == "HelloWorld"

def test_to_header_case_invalid_input():
    with pytest.raises(TypeError):
        to_header_case(123)
    with pytest.raises(TypeError):
        to_header_case(None)