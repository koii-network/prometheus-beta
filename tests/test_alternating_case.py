import pytest
from src.alternating_case import to_alternating_sentence_case

def test_alternating_sentence_case_normal_string():
    assert to_alternating_sentence_case("hello world") == "HeLlO WoRlD"

def test_alternating_sentence_case_empty_string():
    assert to_alternating_sentence_case("") == ""

def test_alternating_sentence_case_single_char():
    assert to_alternating_sentence_case("a") == "A"

def test_alternating_sentence_case_mixed_case():
    assert to_alternating_sentence_case("PytHON ProGRamMIng") == "PyThOn PrOgRaM"

def test_alternating_sentence_case_non_alphabetic():
    assert to_alternating_sentence_case("123 !@#") == "123 !@#"

def test_alternating_sentence_case_invalid_input():
    with pytest.raises(TypeError):
        to_alternating_sentence_case(123)
    with pytest.raises(TypeError):
        to_alternating_sentence_case(None)