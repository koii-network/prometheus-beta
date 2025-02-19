import pytest
from src.pascal_case_converter import to_pascal_case

def test_to_pascal_case_basic_words():
    assert to_pascal_case("hello world") == "HelloWorld"

def test_to_pascal_case_snake_case():
    assert to_pascal_case("snake_case_example") == "SnakeCaseExample"

def test_to_pascal_case_kebab_case():
    assert to_pascal_case("kebab-case-example") == "KebabCaseExample"

def test_to_pascal_case_mixed_delimiters():
    assert to_pascal_case("hello_world-test case") == "HelloWorldTestCase"

def test_to_pascal_case_empty_string():
    assert to_pascal_case("") == ""

def test_to_pascal_case_single_word():
    assert to_pascal_case("python") == "Python"

def test_to_pascal_case_with_numbers():
    assert to_pascal_case("hello2world3test") == "Hello2World3Test"

def test_to_pascal_case_with_special_characters():
    assert to_pascal_case("hello@world#test") == "HelloWorldTest"