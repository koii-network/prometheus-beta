import pytest
from src.alternating_camel_case import alternating_camel_case

def test_standard_string():
    assert alternating_camel_case("hello world") == "hElLo WoRlD"

def test_mixed_case_string():
    assert alternating_camel_case("Python Programming") == "pYtHoN pRoGrAmMiNg"

def test_special_characters():
    assert alternating_camel_case("hello, world! 123") == "hElLo WoRlD"

def test_empty_string():
    assert alternating_camel_case("") == ""

def test_single_character():
    assert alternating_camel_case("a") == "a"

def test_only_special_characters():
    assert alternating_camel_case("!@#$%^") == ""

def test_non_string_input():
    with pytest.raises(TypeError):
        alternating_camel_case(123)

def test_numeric_input():
    assert alternating_camel_case("123 456") == "oNe TwO tHrEe FoUr FiVe SiX"