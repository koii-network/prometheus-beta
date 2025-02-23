import pytest
from src.dot_case_converter import convert_to_dot_case

def test_camel_case_conversion():
    assert convert_to_dot_case("helloWorld") == "hello.world"
    assert convert_to_dot_case("camelCaseString") == "camel.case.string"

def test_pascal_case_conversion():
    assert convert_to_dot_case("HelloWorld") == "hello.world"
    assert convert_to_dot_case("PascalCaseString") == "pascal.case.string"

def test_snake_case_conversion():
    assert convert_to_dot_case("hello_world") == "hello.world"
    assert convert_to_dot_case("snake_case_string") == "snake.case.string"

def test_kebab_case_conversion():
    assert convert_to_dot_case("hello-world") == "hello.world"
    assert convert_to_dot_case("kebab-case-string") == "kebab.case.string"

def test_space_separated_conversion():
    assert convert_to_dot_case("hello world") == "hello.world"
    assert convert_to_dot_case("space separated string") == "space.separated.string"

def test_mixed_case_conversion():
    assert convert_to_dot_case("Hello_World-Test") == "hello.world.test"
    assert convert_to_dot_case("mixedCaseString_with-Separators") == "mixed.case.string.with.separators"

def test_empty_string():
    assert convert_to_dot_case("") == ""

def test_single_word():
    assert convert_to_dot_case("hello") == "hello"
    assert convert_to_dot_case("HELLO") == "hello"

def test_input_type_error():
    with pytest.raises(TypeError):
        convert_to_dot_case(123)
    with pytest.raises(TypeError):
        convert_to_dot_case(None)

def test_already_dot_case():
    assert convert_to_dot_case("already.dot.case") == "already.dot.case"

def test_multiple_consecutive_separators():
    assert convert_to_dot_case("hello__world--test") == "hello.world.test"