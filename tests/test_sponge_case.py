import pytest
from src.sponge_case import to_sponge_case

def test_to_sponge_case_normal_string():
    assert to_sponge_case("hello world") == "hElLo WoRlD"

def test_to_sponge_case_uppercase():
    assert to_sponge_case("PYTHON") == "pYtHoN"

def test_to_sponge_case_mixed_case():
    assert to_sponge_case("PrOgRaMmInG") == "pRoGrAmMiNg"

def test_to_sponge_case_empty_string():
    assert to_sponge_case("") == ""

def test_to_sponge_case_single_character():
    assert to_sponge_case("a") == "a"
    assert to_sponge_case("B") == "b"

def test_to_sponge_case_with_numbers_and_symbols():
    assert to_sponge_case("hello123 world!") == "hElLo123 WoRlD!"