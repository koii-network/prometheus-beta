import pytest
from src.alternating_case import to_alternating_case

def test_basic_alternating_case():
    assert to_alternating_case("hello") == "HeLlO"
    assert to_alternating_case("python") == "PyThOn"

def test_empty_string():
    assert to_alternating_case("") == ""

def test_single_character():
    assert to_alternating_case("a") == "A"
    assert to_alternating_case("B") == "B"

def test_mixed_case_input():
    assert to_alternating_case("HelLo WoRlD") == "HeLlO wOrLd"

def test_non_alphabetic_characters():
    assert to_alternating_case("123!@#") == "123!@#"

def test_invalid_input_type():
    with pytest.raises(TypeError):
        to_alternating_case(123)
    with pytest.raises(TypeError):
        to_alternating_case(None)

def test_unicode_characters():
    assert to_alternating_case("こんにちは") == "コンニチハ"