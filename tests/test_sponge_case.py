import pytest
from src.sponge_case import convert_to_sponge_case

def test_convert_to_sponge_case_normal_string():
    assert convert_to_sponge_case("hello") == "HeLlO"
    assert convert_to_sponge_case("world") == "WoRlD"

def test_convert_to_sponge_case_mixed_case():
    assert convert_to_sponge_case("HelloWorld") == "HeLlOwOrLd"

def test_convert_to_sponge_case_with_spaces():
    assert convert_to_sponge_case("hello world") == "HeLlO WoRlD"

def test_convert_to_sponge_case_with_numbers():
    assert convert_to_sponge_case("hello123world") == "HeLlO123WoRlD"

def test_convert_to_sponge_case_empty_string():
    assert convert_to_sponge_case("") == ""

def test_convert_to_sponge_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_sponge_case(123)
    with pytest.raises(TypeError):
        convert_to_sponge_case(None)