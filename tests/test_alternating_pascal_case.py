import pytest
from src.alternating_pascal_case import to_alternating_pascal_case

def test_basic_conversion():
    assert to_alternating_pascal_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_pascal_case("python is awesome") == "PyThOn Is AwEsOmE"

def test_empty_string():
    assert to_alternating_pascal_case("") == ""

def test_single_word():
    assert to_alternating_pascal_case("python") == "PyThOn"

def test_multiple_words():
    assert to_alternating_pascal_case("this is a test") == "ThIs Is A TeSt"

def test_mixed_case_input():
    assert to_alternating_pascal_case("HELLO world") == "HeLlO WoRlD"
    assert to_alternating_pascal_case("hello WORLD") == "HeLlO WoRlD"

def test_numbers_and_special_characters():
    assert to_alternating_pascal_case("hello 123 world") == "HeLlO 123 WoRlD"
    assert to_alternating_pascal_case("python! is cool") == "PyThOn! Is CoOl"