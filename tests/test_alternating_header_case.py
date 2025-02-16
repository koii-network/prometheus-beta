import pytest
from src.alternating_header_case import to_alternating_header_case

def test_alternating_header_case_basic():
    assert to_alternating_header_case("hello world") == "HeLlO wOrLd"

def test_alternating_header_case_empty_string():
    assert to_alternating_header_case("") == ""

def test_alternating_header_case_non_alphabetic():
    assert to_alternating_header_case("123 abc 456") == "123 AbC 456"

def test_alternating_header_case_mixed_case():
    assert to_alternating_header_case("HELLO world") == "HeLlO wOrLd"

def test_alternating_header_case_type_error():
    with pytest.raises(TypeError):
        to_alternating_header_case(123)

def test_alternating_header_case_special_characters():
    assert to_alternating_header_case("hello, world!") == "HeLlO, WoRlD!"

def test_alternating_header_case_unicode():
    assert to_alternating_header_case("café au lait") == "CaFé Au LaIt"