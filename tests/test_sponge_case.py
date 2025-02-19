import pytest
from src.sponge_case import to_sponge_case

def test_to_sponge_case_basic():
    assert to_sponge_case("hello") == "HeLlO"
    assert to_sponge_case("world") == "WoRlD"

def test_to_sponge_case_empty_string():
    assert to_sponge_case("") == ""

def test_to_sponge_case_with_spaces():
    assert to_sponge_case("hello world") == "HeLlO WoRlD"

def test_to_sponge_case_with_special_chars():
    assert to_sponge_case("hello, world!") == "HeLlO, WoRlD!"

def test_to_sponge_case_invalid_input():
    with pytest.raises(TypeError):
        to_sponge_case(123)
    with pytest.raises(TypeError):
        to_sponge_case(None)